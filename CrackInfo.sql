/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [SHRP_ID]
      ,[DATE_BEGAN]
      ,[SECTION_LENGTH]
      ,[SECTION_WIDTH]
      ,[PERCENT_SEALED]
      ,[LENGTH_SEALED]
      ,[WIDTH_MEAN]
      ,[DEPTH_MEAN]
      ,[LENGTH_PREPARED]
      ,[AVG_WIDTH_CRACK]
      ,[SEAL_THICKNESS]
  FROM [Bucket_30922].[dbo].[SPS3_CRACK]
