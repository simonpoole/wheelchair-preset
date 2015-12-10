#!/bin/bash

FILE=wheelchair_master_preset.xml
[ -e wheelchair_master_preset_grafted.xml ] &&
    FILE=wheelchair_master_preset_grafted.xml

sed "s=ICONPATH:==" < $FILE | sed "s/ICONTYPE/png/" > gen/wheelchair_zip_preset.xml
cd gen
rm  wheelchair.zip
zip wheelchair.zip wheelchair_zip_preset.xml
cd ../icons/png
ls *.png | zip -@ ../../gen/wheelchair.zip 
cd ../../i8n
ls *.po | zip -@ ../gen/wheelchair.zip 

