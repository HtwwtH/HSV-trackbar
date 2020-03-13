# HSV-trackbar
Трэкбар для экспериментов с hsv-диапазоном.

trackbar.py - двигаем ползунки, находим нужные значения hue, saturation, value: h1, s1, v1 и максимальные h2, s2, v2 - смотрим, что будет с картинкой. На картинке будет то, что лежит в этом диапазоне (белым).

main.py - затрем этот объект на ч/б варианте картинки, чтобы он не попадал в область поиска контуров.
(в def find_object вставляем найденные значения hsv_min и hsv_max)

![Trackbar](https://github.com/HtwwtH/HSV-trackbar/blob/master/demonstration/screenshot1.PNG)

![Main](https://github.com/HtwwtH/HSV-trackbar/blob/master/demonstration/screenshot2.PNG)
