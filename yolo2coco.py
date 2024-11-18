import json
import os
import cv2


def yolo2coco(image_dir_path, label_dir_path,save_file_name , is_normalized):

    total = {}

    # make info
    info = {
            'description' : '',
            'url' : '',
            'version' : '',
            'year' : 2020,
            'contributor' : '',
            'data_created' : '2020-04-14 01:45:18.567988'
            }
    total['info'] = info

    # make licenses
    licenses_list = []
    licenses_0= {
            'id' : '1',
            'name' : 'your_name',
            'url' : 'your_name'
            }
    licenses_list.append(licenses_0)

    ''' if you want to add licenses, copy this code
    licenses_1 = {
        'id': '2',
        'name': 'your_name',
        'url': 'your_name'
    }
    licenses_list.append(licenses_1)
    '''

    total['licenses'] = licenses_list

    # make categories
    category_list = []
    class_0 = {
            'id':  1,
            'name' : 'bolt_screw',
            'supercategory' : 'None'
            }
    category_list.append(class_0)

    class_1 = {
            'id':  2,
            'name' : 'nut_washers',
            'supercategory' : 'None'
            }
    category_list.append(class_1)

    class_2 = {
            'id':  3,
            'name' : 'bearing ball',
            'supercategory' : 'None'
            }
    category_list.append(class_2)

    class_3 = {
            'id':  4,
            'name' : 'wire',
            'supercategory' : 'None'
            }
    category_list.append(class_3)

    class_4 = {
            'id':  5,
            'name' : 'feul_lid',
            'supercategory' : 'None'
            }
    category_list.append(class_4)

    class_5 = {
            'id':  6,
            'name' : 'tire_parts',
            'supercategory' : 'None'
            }
    category_list.append(class_5)

    class_6 = {
            'id':  7,
            'name' : 'paper_parts',
            'supercategory' : 'None'
            }
    category_list.append(class_6)

    class_7 = {
            'id':  8,
            'name' : 'plastic_parts',
            'supercategory' : 'None'
            }
    category_list.append(class_7)

    class_8 = {
            'id':  9,
            'name' : 'driver',
            'supercategory' : 'None'
            }
    category_list.append(class_8)

    class_9 = {
            'id':  10,
            'name' : 'wrench',
            'supercategory' : 'None'
            }
    category_list.append(class_9)

    class_10 = {
            'id':  11,
            'name' : 'plier_scissors',
            'supercategory' : 'None'
            }
    category_list.append(class_10)

    class_11 = {
            'id':  12,
            'name' : 'hammer',
            'supercategory' : 'None'
            }
    category_list.append(class_11)

    class_12 = {
            'id':  13,
            'name' : 'drill',
            'supercategory' : 'None'
            }
    category_list.append(class_12)

    class_13 = {
            'id':  14,
            'name' : 'spoon_fork',
            'supercategory' : 'None'
            }
    category_list.append(class_13)

    class_14 = {
            'id':  15,
            'name' : 'paper_cup',
            'supercategory' : 'None'
            }
    category_list.append(class_14)

    class_15 = {
            'id':  16,
            'name' : 'pet_bottle',
            'supercategory' : 'None'
            }
    category_list.append(class_15)

    class_16 = {
            'id':  17,
            'name' : 'can',
            'supercategory' : 'None'
            }
    category_list.append(class_16)

    class_17 = {
            'id':  18,
            'name' : 'pen',
            'supercategory' : 'None'
            }
    category_list.append(class_17)

    class_18 = {
            'id':  19,
            'name' : 'box',
            'supercategory' : 'None'
            }
    category_list.append(class_18)

    class_19 = {
            'id':  20,
            'name' : 'luggage_tag',
            'supercategory' : 'None'
            }
    category_list.append(class_19)

    class_20 = {
            'id':  21,
            'name' : 'clothes',
            'supercategory' : 'None'
            }
    category_list.append(class_20)

    class_21 = {
            'id':  22,
            'name' : 'concrete_stone',
            'supercategory' : 'None'
            }
    category_list.append(class_21)

    class_22 = {
            'id':  23,
            'name' : 'profile',
            'supercategory' : 'None'
            }
    category_list.append(class_22)

    class_23 = {
            'id':  24,
            'name' : 'plastic_bag',
            'supercategory' : 'None'
            }
    category_list.append(class_23)

    class_24 = {
            'id':  25,
            'name' : 'leaf',
            'supercategory' : 'None'
            }
    category_list.append(class_24)

    class_25 = {
            'id':  26,
            'name' : 'branch',
            'supercategory' : 'None'
            }
    category_list.append(class_25)
    '''
    # if you want to add class
    class_1 = {
            'id':  2,
            'name' : 'defect',
            'supercategory' : 'None'
            }
    category_list.append(class_1)
    '''
    total['categories'] = category_list

    # make yolo to coco format

    # get images
    image_list = os.listdir(image_dir_path)
    print('image length : ', len(image_list))
    label_list = os.listdir(label_dir_path)
    print('label length : ',len(label_list))

    image_dict_list = []
    count = 0
    for image_name in image_list :
        img = cv2.imread(image_dir_path+image_name)
        image_dict = {
                'id' : count,
                'file_name' : image_name,
                'width' : img.shape[1],
                'height' : img.shape[0],
                'date_captured' : '2020-04-14 -1:45:18.567975',
                'license' : 1, # put correct license
                'coco_url' : '',
                'flickr_url' : ''
                }
        image_dict_list.append(image_dict)
        count += 1
    total['images'] = image_dict_list

    # make yolo annotation to coco format
    label_dict_list = []
    image_count = 0
    label_count = 0
    for image_name in image_list :
        img = cv2.imread(image_dir_path+image_name)
        label = open(label_dir_path+image_name[0:-4] + '.txt','r')
        if not os.path.isfile(label_dir_path + image_name[0:-4] + '.txt'): # debug code
            print('there is no label match with ',image_dir_path + image_name)
            return
        while True:
            line = label.readline()
            if not line:
                break
            class_number, center_x,center_y,box_width,box_height = line.split()
            # should put bbox x,y,width,height
            # bbox x,y is top left

            if is_normalized :
                center_x =  int(float(center_x) * int(img.shape[1]))
                center_y = int(float(center_y) * int(img.shape[0]))
                box_width = int(float(box_width) * int(img.shape[1]))
                box_height = int(float(box_height) * int(img.shape[0]))
                top_left_x = center_x - int(box_width/2)
                top_left_y = center_y - int(box_height/2)

            if not is_normalized :
                center_x = float(center_x)
                center_y = float(center_y)
                box_width = float(box_width)
                box_height = float(box_height)
                top_left_x = center_x - int(box_width / 2)
                top_left_y = center_y - int(box_height / 2)

            bbox_dict = []
            bbox_dict.append(top_left_x)
            bbox_dict.append(top_left_y)
            bbox_dict.append(box_width)
            bbox_dict.append(box_height)

            # segmetation dict : 8 points to fill, x1,y1,x2,y2,x3,y3,x4,y4
            segmentation_list_list = []
            segmentation_list= []
            segmentation_list.append(bbox_dict[0])
            segmentation_list.append(bbox_dict[1])
            segmentation_list.append(bbox_dict[0] + bbox_dict[2])
            segmentation_list.append(bbox_dict[1])
            segmentation_list.append(bbox_dict[0]+bbox_dict[2])
            segmentation_list.append(bbox_dict[1]+bbox_dict[3])
            segmentation_list.append(bbox_dict[0])
            segmentation_list.append(bbox_dict[1] + bbox_dict[3])
            segmentation_list_list.append(segmentation_list)

            label_dict = {
                    'id' : label_count,
                    'image_id' : image_count,
                    'category_id' : int(class_number)+1,
                    'iscrowd' : 0,
                    'area' : int(bbox_dict[2] * bbox_dict[3]),
                    'bbox' : bbox_dict,
                    'segmentation' : segmentation_list_list
                    }
            label_dict_list.append(label_dict)
            label_count += 1
        label.close()
        image_count += 1

    total['annotations'] = label_dict_list

    with open(save_file_name,'w',encoding='utf-8') as make_file :
        json.dump(total,make_file, ensure_ascii=False,indent='\t')

if __name__ == '__main__':
    image_dir_path = './fod_1107/images/valid_images/'
    label_dir_path = './fod_1107/labels/valid_labels/'
    save_file_name = 'fod_valid.json'
    is_normalized =  True
    # if you want to add more licenses or classes
    # add in code
    yolo2coco(image_dir_path, label_dir_path, save_file_name,is_normalized)

 
