#import geopandas as gpd
#import matplotlib.pyplot as plt


def get_predictions(county):
    predictions = []
    #countyShapes = gpd.read_file("NRI_Shapefile_Counties/NRI_Shapefile_Counties.shp")
    #countyShapes.plot()

    #probably need to pre-generate all the .jpg files and just upload them
    county_img = 'us.jpg'
    #plt.savefig(county_img)
    risk_level = 'TotalRisk: OMG'
    predictions.append(county_img)
    predictions.append(risk_level)
    return predictions
