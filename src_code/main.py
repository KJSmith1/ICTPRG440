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

