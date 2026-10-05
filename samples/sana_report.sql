---- Query 1: Summary Counts ----
WITH
ryb AS (                -- one 6260 enrollment per client
    SELECT p.*,
           ROW_NUMBER() OVER (
               PARTITION BY p.SHISID
               ORDER BY CASE WHEN p.PROGRAM_STATUS = 'A' THEN 0 ELSE 1 END,
                        p.INTAKE_DATE DESC NULLS LAST
           ) AS rn
    FROM Client_Program_Data p
    WHERE p.PRGID = 6260
),
sana AS (               -- SANA history per client
    SELECT cst.SHISID,
           COUNT(*) AS total_sanas,
           LISTAGG(TO_CHAR(cst.SCREEN_DATE, 'MM/DD/YYYY'), ', ')
               WITHIN GROUP (ORDER BY cst.SCREEN_DATE DESC) AS sana_dates
    FROM Client_Screening_Tools cst
    WHERE cst.TESTID = 11272
    GROUP BY cst.SHISID
),
resp AS (               -- earliest active program (excluding 6259) owns the SANA
    SELECT p.SHISID,
           p.PRGID               AS resp_prgid,
           p.LEAD_CLINICIAN_NAME AS resp_provider,
           ROW_NUMBER() OVER (
               PARTITION BY p.SHISID
               ORDER BY p.INTAKE_DATE, p.PRGID
           ) AS rn
    FROM Client_Program_Data p
    WHERE p.PROGRAM_STATUS = 'A'
      AND p.INTAKE_DATE IS NOT NULL
      AND p.PRGID <> 6259
),
prog_counts AS (
    SELECT p.SHISID,
           SUM(CASE WHEN p.PROGRAM_STATUS = 'A' AND p.PRGID <> 6260 THEN 1 ELSE 0 END) AS other_active,
           SUM(CASE WHEN p.PROGRAM_STATUS = 'D' THEN 1 ELSE 0 END)                     AS discharged
    FROM Client_Program_Data p
    GROUP BY p.SHISID
),
base AS (
    SELECT c.SHISID,
           c.Client_ID,
           c.FIRST_NAME,
           c.MI,
           c.LAST_NAME,
           r.Program,
           r.PROGRAM_STATUS,
           r.INTAKE_DATE,
           r.DISCHARGE_DATE,
           NVL(pc.other_active, 0) AS other_active,
           NVL(pc.discharged, 0)   AS discharged,
           NVL(s.total_sanas, 0)   AS total_sanas,
           s.sana_dates,
           CASE
               WHEN r.INTAKE_DATE IS NULL THEN 'Missing Enrollment Date'
               WHEN rs.resp_prgid = 6260  THEN 'YES'
               ELSE 'NO'
           END AS responsible_for_sana,
           CASE WHEN r.INTAKE_DATE IS NOT NULL THEN rs.resp_provider END AS responsible_provider,
           CASE
               WHEN r.PROGRAM_STATUS = 'A' AND r.DISCHARGE_DATE IS NOT NULL THEN 'Active but has discharge date'
               WHEN r.PROGRAM_STATUS = 'D' AND r.DISCHARGE_DATE IS NULL     THEN 'Discharged but no discharge date'
           END AS data_issue
    FROM Clients c
    JOIN ryb r               ON r.SHISID = c.SHISID AND r.rn = 1
    LEFT JOIN sana s         ON s.SHISID = c.SHISID
    LEFT JOIN resp rs        ON rs.SHISID = c.SHISID AND rs.rn = 1
    LEFT JOIN prog_counts pc ON pc.SHISID = c.SHISID
    WHERE NVL(LOWER(TRIM(c.LAST_NAME)), '~') <> 'test'
)
SELECT 'Missing Enrollment Date' AS Label,
       COUNT(CASE WHEN total_sanas = 0 AND responsible_for_sana = 'Missing Enrollment Date' THEN 1 END) AS SANA_Totals
FROM base WHERE PROGRAM_STATUS = 'A'
UNION ALL
SELECT '# of SANAs Responsible For:',
       COUNT(CASE WHEN total_sanas = 0 AND responsible_for_sana = 'YES' THEN 1 END)
FROM base WHERE PROGRAM_STATUS = 'A'
UNION ALL
SELECT 'Active Ptps Missing SANAs:',
       COUNT(CASE WHEN total_sanas = 0 THEN 1 END)
FROM base WHERE PROGRAM_STATUS = 'A'
UNION ALL
SELECT 'Active Ptps w/ a SANA',
       COUNT(CASE WHEN total_sanas > 0 THEN 1 END)
FROM base WHERE PROGRAM_STATUS = 'A'
UNION ALL
SELECT 'Records with Status/Discharge Mismatch',
       COUNT(data_issue)
FROM base;

---- Query 2: Active Participants Missing SANAs ----
WITH
ryb AS (
    SELECT p.*,
           ROW_NUMBER() OVER (
               PARTITION BY p.SHISID
               ORDER BY CASE WHEN p.PROGRAM_STATUS = 'A' THEN 0 ELSE 1 END,
                        p.INTAKE_DATE DESC NULLS LAST
           ) AS rn
    FROM Client_Program_Data p
    WHERE p.PRGID = 6260
),
sana AS (
    SELECT cst.SHISID,
           COUNT(*) AS total_sanas,
           LISTAGG(TO_CHAR(cst.SCREEN_DATE, 'MM/DD/YYYY'), ', ')
               WITHIN GROUP (ORDER BY cst.SCREEN_DATE DESC) AS sana_dates
    FROM Client_Screening_Tools cst
    WHERE cst.TESTID = 11272
    GROUP BY cst.SHISID
),
resp AS (
    SELECT p.SHISID,
           p.PRGID               AS resp_prgid,
           p.LEAD_CLINICIAN_NAME AS resp_provider,
           ROW_NUMBER() OVER (
               PARTITION BY p.SHISID
               ORDER BY p.INTAKE_DATE, p.PRGID
           ) AS rn
    FROM Client_Program_Data p
    WHERE p.PROGRAM_STATUS = 'A'
      AND p.INTAKE_DATE IS NOT NULL
      AND p.PRGID <> 6259
),
prog_counts AS (
    SELECT p.SHISID,
           SUM(CASE WHEN p.PROGRAM_STATUS = 'A' AND p.PRGID <> 6260 THEN 1 ELSE 0 END) AS other_active,
           SUM(CASE WHEN p.PROGRAM_STATUS = 'D' THEN 1 ELSE 0 END)                     AS discharged
    FROM Client_Program_Data p
    GROUP BY p.SHISID
),
base AS (
    SELECT c.SHISID,
           c.Client_ID,
           c.FIRST_NAME,
           c.MI,
           c.LAST_NAME,
           r.Program,
           r.PROGRAM_STATUS,
           r.INTAKE_DATE,
           r.DISCHARGE_DATE,
           NVL(pc.other_active, 0) AS other_active,
           NVL(pc.discharged, 0)   AS discharged,
           NVL(s.total_sanas, 0)   AS total_sanas,
           s.sana_dates,
           CASE
               WHEN r.INTAKE_DATE IS NULL THEN 'Missing Enrollment Date'
               WHEN rs.resp_prgid = 6260  THEN 'YES'
               ELSE 'NO'
           END AS responsible_for_sana,
           CASE WHEN r.INTAKE_DATE IS NOT NULL THEN rs.resp_provider END AS responsible_provider,
           CASE
               WHEN r.PROGRAM_STATUS = 'A' AND r.DISCHARGE_DATE IS NOT NULL THEN 'Active but has discharge date'
               WHEN r.PROGRAM_STATUS = 'D' AND r.DISCHARGE_DATE IS NULL     THEN 'Discharged but no discharge date'
           END AS data_issue
    FROM Clients c
    JOIN ryb r               ON r.SHISID = c.SHISID AND r.rn = 1
    LEFT JOIN sana s         ON s.SHISID = c.SHISID
    LEFT JOIN resp rs        ON rs.SHISID = c.SHISID AND rs.rn = 1
    LEFT JOIN prog_counts pc ON pc.SHISID = c.SHISID
    WHERE NVL(LOWER(TRIM(c.LAST_NAME)), '~') <> 'test'
)
SELECT SHISID                                  AS EHR_ID,
       Client_ID,
       Program                                 AS Program_Name,
       'Active'                                AS Program_Status,
       TO_CHAR(INTAKE_DATE, 'MM/DD/YYYY')      AS Enrollment_Date,
       TO_CHAR(DISCHARGE_DATE, 'MM/DD/YYYY')   AS Discharge_Date,
       FIRST_NAME                              AS First_Name,
       MI                                      AS Middle_Name,
       LAST_NAME                               AS Last_Name,
       other_active                            AS NUM_Of_Other_Active_Programs,
       discharged                              AS NUM_Of_Discharged_Programs,
       responsible_for_sana                    AS Program_RESPONSIBLE_FOR_SANA,
       responsible_provider                    AS Responsible_Provider,
       data_issue                              AS Data_Issue,
       'Missing SANA'                          AS Test_Name
FROM base
WHERE PROGRAM_STATUS = 'A'
  AND total_sanas = 0
ORDER BY INTAKE_DATE DESC NULLS FIRST, LAST_NAME, FIRST_NAME;

---- Query 3: Active Participants w/ a SANA ----
WITH
ryb AS (
    SELECT p.*,
           ROW_NUMBER() OVER (
               PARTITION BY p.SHISID
               ORDER BY CASE WHEN p.PROGRAM_STATUS = 'A' THEN 0 ELSE 1 END,
                        p.INTAKE_DATE DESC NULLS LAST
           ) AS rn
    FROM Client_Program_Data p
    WHERE p.PRGID = 6260
),
sana AS (
    SELECT cst.SHISID,
           COUNT(*) AS total_sanas,
           LISTAGG(TO_CHAR(cst.SCREEN_DATE, 'MM/DD/YYYY'), ', ')
               WITHIN GROUP (ORDER BY cst.SCREEN_DATE DESC) AS sana_dates
    FROM Client_Screening_Tools cst
    WHERE cst.TESTID = 11272
    GROUP BY cst.SHISID
),
resp AS (
    SELECT p.SHISID,
           p.PRGID               AS resp_prgid,
           p.LEAD_CLINICIAN_NAME AS resp_provider,
           ROW_NUMBER() OVER (
               PARTITION BY p.SHISID
               ORDER BY p.INTAKE_DATE, p.PRGID
           ) AS rn
    FROM Client_Program_Data p
    WHERE p.PROGRAM_STATUS = 'A'
      AND p.INTAKE_DATE IS NOT NULL
      AND p.PRGID <> 6259
),
prog_counts AS (
    SELECT p.SHISID,
           SUM(CASE WHEN p.PROGRAM_STATUS = 'A' AND p.PRGID <> 6260 THEN 1 ELSE 0 END) AS other_active,
           SUM(CASE WHEN p.PROGRAM_STATUS = 'D' THEN 1 ELSE 0 END)                     AS discharged
    FROM Client_Program_Data p
    GROUP BY p.SHISID
),
base AS (
    SELECT c.SHISID,
           c.Client_ID,
           c.FIRST_NAME,
           c.MI,
           c.LAST_NAME,
           r.Program,
           r.PROGRAM_STATUS,
           r.INTAKE_DATE,
           r.DISCHARGE_DATE,
           NVL(pc.other_active, 0) AS other_active,
           NVL(pc.discharged, 0)   AS discharged,
           NVL(s.total_sanas, 0)   AS total_sanas,
           s.sana_dates,
           CASE
               WHEN r.INTAKE_DATE IS NULL THEN 'Missing Enrollment Date'
               WHEN rs.resp_prgid = 6260  THEN 'YES'
               ELSE 'NO'
           END AS responsible_for_sana,
           CASE WHEN r.INTAKE_DATE IS NOT NULL THEN rs.resp_provider END AS responsible_provider,
           CASE
               WHEN r.PROGRAM_STATUS = 'A' AND r.DISCHARGE_DATE IS NOT NULL THEN 'Active but has discharge date'
               WHEN r.PROGRAM_STATUS = 'D' AND r.DISCHARGE_DATE IS NULL     THEN 'Discharged but no discharge date'
           END AS data_issue
    FROM Clients c
    JOIN ryb r               ON r.SHISID = c.SHISID AND r.rn = 1
    LEFT JOIN sana s         ON s.SHISID = c.SHISID
    LEFT JOIN resp rs        ON rs.SHISID = c.SHISID AND rs.rn = 1
    LEFT JOIN prog_counts pc ON pc.SHISID = c.SHISID
    WHERE NVL(LOWER(TRIM(c.LAST_NAME)), '~') <> 'test'
)
SELECT SHISID                                  AS EHR_ID,
       Client_ID,
       Program                                 AS Program_Name,
       'Active'                                AS Program_Status,
       TO_CHAR(INTAKE_DATE, 'MM/DD/YYYY')      AS Enrollment_Date,
       TO_CHAR(DISCHARGE_DATE, 'MM/DD/YYYY')   AS Discharge_Date,
       FIRST_NAME                              AS First_Name,
       MI                                      AS Middle_Name,
       LAST_NAME                               AS Last_Name,
       other_active                            AS NUM_Of_Other_Active_Programs,
       discharged                              AS NUM_Of_Discharged_Programs,
       responsible_for_sana                    AS Program_RESPONSIBLE_FOR_SANA,
       responsible_provider                    AS Responsible_Provider,
       total_sanas                             AS TOTAL_SANAs,
       sana_dates                              AS SANA_DATES,
       data_issue                              AS Data_Issue
FROM base
WHERE PROGRAM_STATUS = 'A'
  AND total_sanas > 0
ORDER BY INTAKE_DATE DESC NULLS FIRST, LAST_NAME, FIRST_NAME;
