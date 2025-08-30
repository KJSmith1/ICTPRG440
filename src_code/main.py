def readSpatialDataReturnGeodataframe(inputPath):

    if isinstance(inputPath, str):
        pass
    else:
        raise ValueError ("input file path is not a string")
    
    from geopandas import read_file
    
    inputGdf = read_file(inputPath)

    return inputGdf
    
