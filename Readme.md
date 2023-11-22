# Split dataset into Train, Valid and test
If you have any dataset of images and json/xml(annotations) formate, you have to split it into train, valid and test. You can use this [script](split_data.py), it will split your dataset with with configurable split percentage and save it into train, valid and test folder with images and lables folders. 

### You have to change your path for input dataset.
```
images_path = "path/to/images/folder"
labels_path = "path/to/labels/folder"
```

### Also you can change percentage values with which you want to split dataset into train, valid and test.
```
# 70% train, 20% test and 10% valid
train, test, valid = 0.7, 0.2, 0.1
```

## folder structure

### input folder structure
``` 
├── images
|── labels
```

### output folder structure
```
├── train
│   ├── images
│   └── labels
├── valid
│   ├── images
│   └── labels
└── test
    ├── images
    └── labels
```
