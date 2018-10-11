#!/bin/python
import  asciichartpy

array = [16.65999984741211, 16.3799991607666, 16.959999084472656, 16.959999084472656, 16.920000076293945, 16.84000015258789, 16.579999923706055, 17.020000457763672, 18.260000228881836, 18.280000686645508, 18.299999237060547, 18.81999969482422, 18.700000762939453, 18.799999237060547, 18.5, 19.440000534057617, 19.15999984741211, 18.940000534057617, 19.18000030517578, 19.5, 19.040000915527344, 19.3799991607666, 19.299999237060547, 19.600000381469727, 19.479999542236328, 19.5, 19.31999969482422, 19.280000686645508, 19.600000381469727, 20.799999237060547, 21.100000381469727, 21.049999237060547, 21.700000762939453, 21.200000762939453, 21.100000381469727, 19.920000076293945, 21.25, 21.100000381469727, 21.0, 20.850000381469727, 20.799999237060547, 21.049999237060547, 21.450000762939453, 20.899999618530273, 21.25, 21.25, 21.100000381469727, 21.0, 21.0, 21.399999618530273, 21.899999618530273, 21.850000381469727, 21.950000762939453, 22.0, 21.799999237060547, 21.649999618530273, 21.75, 20.100000381469727, 20.299999237060547, 20.149999618530273, 20.350000381469727, 20.200000762939453, 20.25, 20.149999618530273, 19.739999771118164, 19.68000030517578, 19.639999389648438, 19.959999084472656, 19.84000015258789, 19.920000076293945, 19.899999618530273, 19.479999542236328, 19.6200008392334, 19.6200008392334, 19.65999984741211, 19.440000534057617, 19.280000686645508, 19.1200008392334, 19.5, 19.459999084472656, 19.360000610351562, 19.200000762939453, 19.0, 18.579999923706055, 18.579999923706055, 18.520000457763672, 18.760000228881836, 18.559999465942383, 18.31999969482422, 18.260000228881836, 18.5, 18.799999237060547, 18.360000610351562, 18.399999618530273, 18.34000015258789, 18.139999389648438, 18.18000030517578, 18.280000686645508, 18.31999969482422, 19.079999923706055, 18.920000076293945, 18.940000534057617, 18.8799991607666, 18.899999618530273, 18.979999542236328, 18.899999618530273, 18.579999923706055, 18.479999542236328, 18.479999542236328, 18.579999923706055, 18.5, 18.600000381469727, 18.420000076293945, 17.600000381469727, 17.559999465942383, 17.540000915527344, 17.520000457763672, 17.559999465942383, 17.799999237060547, 17.940000534057617, 17.760000228881836, 17.68000030517578, 17.780000686645508, 17.8799991607666, 18.1200008392334, 17.860000610351562, 18.0, 17.579999923706055, 17.18000030517578, 17.040000915527344, 17.059999465942383, 17.200000762939453, 17.260000228881836, 17.459999084472656, 17.18000030517578, 17.059999465942383, 17.059999465942383, 17.020000457763672, 17.059999465942383, 17.040000915527344, 17.200000762939453, 17.540000915527344, 17.459999084472656, 17.399999618530273, 17.200000762939453, 17.239999771118164, 17.219999313354492, 17.299999237060547, 17.31999969482422, 17.420000076293945, 17.420000076293945, 17.399999618530273, 17.479999542236328, 17.600000381469727, 17.540000915527344, 17.559999465942383, 17.540000915527344, 17.540000915527344, 17.5, 17.200000762939453, 17.219999313354492, 17.3799991607666, 17.479999542236328, 17.81999969482422, 18.100000381469727, 18.219999313354492, 18.100000381469727, 18.1200008392334, 18.299999237060547, 18.360000610351562, 18.299999237060547, 18.280000686645508, 18.040000915527344, 18.079999923706055, 18.18000030517578, 18.0, 17.739999771118164, 17.399999618530273, 17.360000610351562, 17.479999542236328, 17.459999084472656, 17.520000457763672, 17.600000381469727, 17.280000686645508, 17.139999389648438, 17.18000030517578, 17.1200008392334, 17.15999984741211, 17.18000030517578, 17.280000686645508, 16.399999618530273, 16.31999969482422, 16.3799991607666, 16.34000015258789, 16.360000610351562, 16.34000015258789, 16.15999984741211, 16.280000686645508, 16.040000915527344, 16.020000457763672, 16.079999923706055, 16.079999923706055, 16.059999465942383, 16.600000381469727, 16.5, 16.360000610351562, 16.399999618530273, 16.360000610351562, 16.360000610351562, 16.3799991607666, 16.579999923706055, 16.639999389648438, 16.520000457763672, 16.5, 16.540000915527344, 16.34000015258789, 16.399999618530273, 16.780000686645508, 16.719999313354492, 17.059999465942383, 17.020000457763672, 17.18000030517578, 17.280000686645508, 17.360000610351562, 17.739999771118164, 17.5, 17.5, 17.579999923706055, 17.579999923706055, 17.579999923706055, 17.65999984741211, 18.239999771118164, 18.139999389648438, 17.940000534057617, 17.959999084472656, 18.040000915527344, 18.020000457763672, 17.520000457763672, 17.200000762939453, 17.020000457763672, 17.059999465942383, 17.079999923706055, 17.15999984741211, 17.15999984741211, 17.079999923706055, 17.34000015258789, 17.260000228881836, 17.3799991607666, 17.360000610351562, 17.399999618530273, 17.420000076293945, 17.420000076293945, 17.579999923706055, 17.260000228881836, 17.059999465942383, 17.079999923706055, 17.079999923706055, 17.040000915527344, 17.100000381469727, 17.100000381469727, 17.1200008392334, 17.100000381469727, 17.15999984741211, 17.139999389648438, 17.1200008392334, 17.139999389648438, 17.280000686645508, 17.15999984741211, 17.079999923706055, 17.100000381469727, 17.079999923706055, 17.139999389648438, 17.100000381469727, 16.860000610351562, 16.639999389648438, 16.719999313354492, 16.739999771118164, 16.739999771118164, 16.780000686645508, 16.81999969482422, 16.799999237060547, 16.600000381469727, 16.600000381469727, 16.520000457763672, 16.540000915527344, 16.479999542236328, 16.5, 16.600000381469727, 16.719999313354492, 16.719999313354492, 16.760000228881836, 16.81999969482422, 16.8799991607666, 16.780000686645508, 16.719999313354492, 16.639999389648438, 16.579999923706055, 16.579999923706055, 16.6200008392334, 16.600000381469727, 16.540000915527344, 16.579999923706055, 16.6200008392334, 16.739999771118164, 16.799999237060547, 16.6200008392334, 16.559999465942383, 16.479999542236328, 16.5, 16.540000915527344, 16.5, 16.3799991607666, 16.420000076293945, 16.399999618530273, 16.5, 16.5, 15.9399995803833, 16.1200008392334, 16.139999389648438, 16.1200008392334, 16.0, 16.059999465942383, 16.1200008392334, 16.079999923706055, 16.139999389648438, 16.15999984741211, 16.100000381469727, 16.15999984741211, 16.1200008392334, 16.200000762939453, 16.100000381469727, 16.079999923706055, 16.040000915527344, 16.0, 16.040000915527344, 15.920000076293945, 16.020000457763672, 16.020000457763672, 16.020000457763672, 16.079999923706055, 16.1200008392334, 16.200000762939453, 16.34000015258789, 16.68000030517578, 16.799999237060547, 16.639999389648438, 16.700000762939453, 16.65999984741211, 16.65999984741211, 16.639999389648438, 16.5, 16.299999237060547, 16.219999313354492, 16.280000686645508, 16.260000228881836, 16.5, 16.479999542236328, 16.440000534057617, 16.360000610351562, 16.139999389648438, 16.100000381469727, 16.18000030517578, 16.3799991607666, 16.219999313354492, 16.399999618530273, 16.399999618530273, 16.479999542236328, 16.440000534057617, 16.440000534057617, 16.440000534057617, 16.479999542236328, 16.540000915527344, 16.559999465942383, 16.3799991607666, 16.299999237060547, 16.3799991607666, 16.399999618530273, 16.479999542236328, 16.600000381469727, 16.5, 16.559999465942383, 16.520000457763672, 16.579999923706055, 16.68000030517578, 16.65999984741211, 16.6200008392334, 16.420000076293945, 16.399999618530273, 16.3799991607666, 16.360000610351562, 16.31999969482422, 16.440000534057617, 16.440000534057617, 16.34000015258789, 16.399999618530273, 16.399999618530273, 16.420000076293945, 16.360000610351562, 16.399999618530273, 16.3799991607666, 16.219999313354492, 16.139999389648438, 16.040000915527344, 16.079999923706055, 16.059999465942383, 16.020000457763672, 16.020000457763672, 15.5600004196167, 15.479999542236328, 15.5, 15.520000457763672, 15.5600004196167, 15.539999961853027, 15.600000381469727, 15.279999732971191, 15.119999885559082, 15.100000381469727, 15.039999961853027, 14.960000038146973, 15.0, 15.0, 14.819999694824219, 14.640000343322754, 14.640000343322754, 14.699999809265137, 14.699999809265137, 14.800000190734863, 14.84000015258789, 14.479999542236328, 14.460000038146973, 14.4399995803833, 14.399999618530273, 14.359999656677246, 14.380000114440918, 14.15999984741211, 14.0600004196167, 14.100000381469727, 14.140000343322754, 14.100000381469727, 14.239999771118164, 14.220000267028809, 14.260000228881836, 13.699999809265137, 13.739999771118164, 13.720000267028809, 13.760000228881836, 13.640000343322754, 13.5600004196167, 13.760000228881836, 13.819999694824219, 13.899999618530273, 13.899999618530273, 13.899999618530273, 13.779999732971191, 13.619999885559082, 13.699999809265137, 13.899999618530273, 13.779999732971191, 13.760000228881836, 13.859999656677246, 13.760000228881836, 13.760000228881836, 12.979999542236328, 12.720000267028809, 12.5600004196167, 12.479999542236328, 12.399999618530273, 12.420000076293945, 12.65999984741211]

print(array)
print(len(array))

while len(array) >= 70:
    for x in range(len(array)):
       # print(array[x])
        if x %3 == 0 and x < len(array):
            del array[x]
#            if x >= len(array):
#                break
         #   print("work")
            #print("leng:",len(array))



print(array)
print(len(array))
print(asciichartpy.plot(array, {'height': 10}))