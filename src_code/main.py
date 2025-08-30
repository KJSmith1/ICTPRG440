def readSpatialDataReturnGeodataframe(inputPath):

    """
    This function reads a spatial data file (e.g., shapefile, kml) 
    from "inputPath" (a string with prefix "r") and returns
    "inputGdf" (a geodataframe)
    """
    import geopandas as gpd

    #validate that inputPath is a string
    if isinstance(inputPath, str):
        pass
    else:
        raise ValueError ("input file path is not a string")
    
    #validate read file function
    try:
        inputGdf = gpd.read_file(inputPath)
    except Exception as e:
        print(".......Error.......\n", e)

    #validate that output is a geodataframe
    if isinstance(inputGdf, gpd.GeoDataFrame):
        pass
    else:
        raise ValueError ("object returned from readSpatialDataReturnGeodataframe is not a geodataframe")

    return inputGdf

def printAllAttributeRows(inputPath):

    """ 
    This function reads a spatial data file (e.g., shapefile, kml) 
    from "inputPath" (a string with prefix "r"), converts it to a geodataframe object
    and prints each row of the attribute table for that object to the console
    in PandasNamedTuple format.
    Returns None.
    """
    #call the function that reads a spatial data file and returns the geodataframe "inputGdf" 
    inputGdf = readSpatialDataReturnGeodataframe(inputPath)

    #print each row of the attribute table in the object returned by readSpatialDataReturnGeodataframe()
    for row in inputGdf.itertuples():
        print(row)
    
    return None

def projectCoordinatesOutputShapefile(inputPath, outputPath, EPSG=9473):

    """
    This function reads a spatial data file (e.g., shapefile, kml) 
    from "inputPath" (a string with prefix "r"), converts it to a geodataframe object, 
    projects the coordinates of that object to the specified 
    "EPSG" (an integer, default = 9473 [GDA2020 Australian Albers])
    and saves the projected object as a shapefile in 
    "outputPath" (a string).
    Returns None.
    """
    import geopandas as gpd

    #call the function that reads a spatial data file and returns the geodataframe "inputGdf" 
    readSpatialDataReturnGeodataframe(inputPath)

    #validate that outputPath is a string
    if isinstance(outputPath, str):
        pass
    else:
        raise ValueError ("output file path is not a string")
    
    #validate that EPSG parameter is an integer
    if isinstance(EPSG, int):
        pass
    else:
        raise ValueError ("EPSG is not an integer")
    
    #validate function for projection to the specified coordinate system
    try:
        projectedGdf = inputGdf.to_crs(epsg=EPSG)
    except Exception as e:
        print(".......Error.......\n", e)
    
    #validate the projected object is a geodataframe
    if isinstance(projectedGdf, gpd.GeoDataFrame):
        pass
    else:
        raise ValueError ("projected object is not a geodataframe")
    
    #retrive original file name from inputPath and define the output file path
    from ntpath import basename
    outputFile = outputPath + "\\" + basename(inputPath) + ".shp"

    #save the projected object as a shapefile in the specified output location
    projectedGdf.to_file(outputFile, driver="ESRI Shapefile")

    return None

printAllAttributeRows (
    r"C:\Users\kovid\Documents\GitHub\ICTPRG440\spatial_data_original\72995a8b-2b81-4656-83d1-9b53a99ff77a\NSW_NPWS_Fuel_Hazard.shp")

    
    
    
