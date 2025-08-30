def readSpatialDataReturnGeodataframe(inputPath):

    if isinstance(inputPath, str):
        pass
    else:
        raise ValueError ("input file path is not a string")
    
    from geopandas import read_file
    
    inputGdf = read_file(inputPath)

    return inputGdf
    
def printAllAttributeRows(inputPath):

    readSpatialDataReturnGeodataframe(inputPath)

    from pandas import DataFrame

    if isinstance(inputGdf, DataFrame):
        pass
    else:
        raise ValueError ("object returned from readSpatialDataReturnGeodataframe is not a geodataframe")
    
    for row in inputGdf:
        print(row)
    
    return None

def projectCoordinatesOutputShapefile(inputPath, outputPath, EPSG=9473):

    readSpatialDataReturnGeodataframe(inputPath)

    from pandas import DataFrame

    if isinstance(inputGdf, DataFrame):
        pass
    else:
        raise ValueError ("object returned from readSpatialDataReturnGeodataframe is not a geodataframe")
    
    if isinstance(outputPath, str):
        pass
    else:
        raise ValueError ("output file path is not a string")
    
    if isinstance(EPSG, int):
        pass
    else:
        raise ValueError ("EPSG is not an integer")
    
    try:
        projectedGdf = inputGdf.to_crs(epsg=EPSG)
    except Exception as e:
        print(".......Error.......\n", e)
    
    if isinstance(projectedGdf, DataFrame):
        pass
    else:
        raise ValueError ("projected object is not a geodataframe")
    
    from ntpath import basename
    
    outputFile = outputPath + "\\" + basename(inputPath) + ".shp"

    projectedGdf.to_file(outputFile, driver="ESRI Shapefile")

    return None



    
    
    
