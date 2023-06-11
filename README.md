## Thisfunctionality is without geo coordinates 

## Instruction
1. **node -v** need to be 16.18.0
2. npm install (if you will get such error " throw new Error('library dir does not exist: ' + libDir)" go please to "Problem with openCV on ubuntu 22.04, fix errror" or how to install on your os openCV (https://github.com/justadudewhohacks/opencv4nodejs))
3. create folder "uploads" in root folder near with "src"
4. npm run start:dev - to start server, your project will look like this:
![image](https://github.com/Skitus/openCV/assets/80597741/53afc641-2eec-47a0-93f2-8d249d4f3aa5)

5. go to postman and use such query (it`s really important to name field "files" and put here 2 photos that will a get a little same place)
![image](https://github.com/Skitus/openCV/assets/80597741/84fef7f7-7fa6-4968-abf0-b9cf13a75003)
6. after success you will get "ortophoto.jpg" with created orthomosaic 

Problem with openCV on ubuntu 22.04, fix errror:

**sudo apt-get update**

**sudo apt-get upgrade**

**sudo apt-get install cmake g++ wget unzip**

**wget https://github.com/opencv/opencv/archive/refs/tags/4.5.3.zip**
**unzip 4.5.3.zip**

**mkdir -p build && cd build**

**cmake ../opencv-4.5.3**

**make -j4**

**sudo make install**

**npm install --save opencv4nodejs**

OR

export OPENCV4NODEJS_DISABLE_AUTOBUILD=1

export OPENCV_INCLUDE_DIR=/usr/local/include

export OPENCV_LIB_DIR=/usr/local/lib

export OPENCV_BIN_DIR=/usr/local/bin

npm install --save opencv4nodejs
 

Also alternative and tried ways to get finish target:
Pix4D: Pix4D is software for image processing and generating orthophotoplans and 3D models from aerial photographs. It supports automatic georeferencing and enables the creation of orthophotoplans without the need for manual intervention.

Agisoft Metashape: Agisoft Metashape (previously known as Photoscan) is another powerful tool for creating orthophotoplans and 3D models. It also offers automatic georeferencing capabilities and allows manual adjustment of processing parameters.

Erdas Imagine: Erdas Imagine is a comprehensive geospatial platform for processing and analyzing geospatial data, including aerial photographs. It enables the creation of orthophotoplans and provides georeferencing functionality.

Global Mapper: Global Mapper is a geospatial program with a wide range of features, including the ability to process aerial photographs and generate orthophotoplans. It also supports georeferencing and can work with various data formats.

ArcGIS: ArcGIS is a geospatial information system platform that offers extensive capabilities for processing and analyzing geospatial data. With ArcGIS, you can create orthophotoplans and perform georeferencing of aerial photographs.

## OpenCV vs Pix4D:

Main disadvantage we don`t have it on node (we can not install it using npm)

Application Focus:

Pix4D: Pix4D is specialized software for photogrammetry and aerial image processing. It is designed specifically for generating accurate orthophotoplans and 3D models from aerial photographs.
OpenCV: OpenCV is a versatile computer vision library that provides a wide range of functionalities for image and video processing. It is not specifically designed for processing aerial photographs or generating orthophotoplans but can be used for general computer vision tasks.
Functionality:

Pix4D: Pix4D offers automated workflows and advanced algorithms for photogrammetric processing. It provides features such as automated georeferencing, dense point cloud generation, 3D modeling, and orthophotoplan generation.
OpenCV: OpenCV provides a comprehensive set of functions and algorithms for computer vision tasks such as image manipulation, feature detection, object recognition, and image analysis. It does not have built-in functionalities for specific aerial photogrammetry tasks.
Georeferencing:

Pix4D: Pix4D includes automated georeferencing capabilities, allowing the generated orthophotoplans and 3D models to be accurately georeferenced to real-world coordinates.
OpenCV: OpenCV does not have built-in georeferencing functionalities. It focuses more on computer vision algorithms and does not have specific features for handling geographic information.
User Interface:

Pix4D: Pix4D provides a user-friendly interface with a dedicated GUI that streamlines the photogrammetric processing workflow. It offers intuitive tools for project management, data visualization, and result analysis.
OpenCV: OpenCV primarily provides a library of functions and does not include a graphical user interface. It is designed to be used programmatically and integrated into custom applications or scripts.
Industry Adoption:

Pix4D: Pix4D is widely adopted in industries such as surveying, mapping, agriculture, construction, and infrastructure inspection. It is specifically tailored for professionals working with aerial imagery and geospatial data.
OpenCV: OpenCV is widely used in computer vision research, robotics, automation, and general-purpose image processing applications. It has a broad user base across various industries and academic fields.

Overall, the main difference between Pix4D and OpenCV lies in their specific focus and functionality. Pix4D is a specialized software dedicated to photogrammetry and aerial image processing, providing automated workflows and georeferencing capabilities. OpenCV, on the other hand, is a versatile computer vision library that offers a broad range of functions for general image and video processing tasks but lacks specialized features for photogrammetry and geospatial analysis.

## OpenCV vs Agisoft Metashape :

Main disadvantage we don`t have it on node (we can not install it using npm)

Application Focus:

Agisoft Metashape: Agisoft Metashape is a specialized photogrammetry software designed for generating accurate orthophotoplans and 3D models from photographs. It focuses on processing aerial and ground-based imagery for various applications such as mapping, surveying, and cultural heritage documentation.
OpenCV: OpenCV is a versatile computer vision library that provides a wide range of functions and algorithms for image and video processing. It is not specifically designed for photogrammetry but offers general-purpose tools for computer vision tasks.
Photogrammetric Capabilities:

Agisoft Metashape: Agisoft Metashape offers advanced photogrammetric functionalities, including automated camera calibration, dense point cloud generation, mesh reconstruction, texture mapping, and orthophotoplan generation. It provides specific tools and workflows for processing image collections to create accurate 3D models.
OpenCV: OpenCV does not have built-in functionalities for photogrammetry. While it provides basic image processing functions, feature detection, and matching algorithms that are relevant to photogrammetry, it does not offer specialized tools for the complete photogrammetric pipeline.
User Interface:

Agisoft Metashape: Agisoft Metashape provides a user-friendly graphical user interface (GUI) that allows users to manage projects, visualize data, adjust processing parameters, and analyze results. It offers an intuitive workflow for photogrammetric processing and model creation.
OpenCV: OpenCV primarily provides a library of functions and does not include a GUI. It is designed to be used programmatically, requiring developers to write code and integrate OpenCV functions into their own applications or scripts.
Industry Adoption:

Agisoft Metashape: Agisoft Metashape is widely adopted in industries such as geospatial mapping, surveying, cultural heritage preservation, and virtual reality. It is recognized as a leading software for photogrammetric processing and 3D model generation.
OpenCV: OpenCV is widely used in computer vision research, robotics, automation, and general-purpose image processing applications. It has a broad user base across various industries and academic fields.

Overall, the main difference between Agisoft Metashape and OpenCV lies in their specific focus and capabilities. Agisoft Metashape is dedicated to photogrammetric processing, offering specialized tools and a user-friendly interface for creating accurate orthophotoplans and 3D models. OpenCV, on the other hand, is a versatile computer vision library that provides a wide range of functions for general image processing tasks but lacks the specialized features and workflows specific to photogrammetry.

## OpenCV vs Agisoft Metashape :

Main disadvantage we don`t have it on node (we can not install it using npm)

Application Focus:

Agisoft Metashape: Agisoft Metashape is a specialized photogrammetry software designed for generating accurate orthophotoplans and 3D models from photographs. It focuses on processing aerial and ground-based imagery for various applications such as mapping, surveying, and cultural heritage documentation.
OpenCV: OpenCV is a versatile computer vision library that provides a wide range of functions and algorithms for image and video processing. It is not specifically designed for photogrammetry but offers general-purpose tools for computer vision tasks.
Photogrammetric Capabilities:

Agisoft Metashape: Agisoft Metashape offers advanced photogrammetric functionalities, including automated camera calibration, dense point cloud generation, mesh reconstruction, texture mapping, and orthophotoplan generation. It provides specific tools and workflows for processing image collections to create accurate 3D models.
OpenCV: OpenCV does not have built-in functionalities for photogrammetry. While it provides basic image processing functions, feature detection, and matching algorithms that are relevant to photogrammetry, it does not offer specialized tools for the complete photogrammetric pipeline.
User Interface:

Agisoft Metashape: Agisoft Metashape provides a user-friendly graphical user interface (GUI) that allows users to manage projects, visualize data, adjust processing parameters, and analyze results. It offers an intuitive workflow for photogrammetric processing and model creation.
OpenCV: OpenCV primarily provides a library of functions and does not include a GUI. It is designed to be used programmatically, requiring developers to write code and integrate OpenCV functions into their own applications or scripts.
Industry Adoption:

Agisoft Metashape: Agisoft Metashape is widely adopted in industries such as geospatial mapping, surveying, cultural heritage preservation, and virtual reality. It is recognized as a leading software for photogrammetric processing and 3D model generation.
OpenCV: OpenCV is widely used in computer vision research, robotics, automation, and general-purpose image processing applications. It has a broad user base across various industries and academic fields.

Overall, the main difference between Agisoft Metashape and OpenCV lies in their specific focus and capabilities. Agisoft Metashape is dedicated to photogrammetric processing, offering specialized tools and a user-friendly interface for creating accurate orthophotoplans and 3D models. OpenCV, on the other hand, is a versatile computer vision library that provides a wide range of functions for general image processing tasks but lacks the specialized features and workflows specific to photogrammetry.

## OpenCV vs Erdas Imagine:

Main disadvantage we don`t have it on node (we can not install it using npm)

Application Focus:

Erdas Imagine: Erdas Imagine is a comprehensive geospatial platform specifically designed for processing and analyzing geospatial data, including aerial photographs and remote sensing imagery. It offers a wide range of tools and functionalities for geospatial analysis, image classification, change detection, and spatial modeling.
OpenCV: OpenCV is a versatile computer vision library that provides a broad set of functions and algorithms for general-purpose image and video processing, as well as computer vision tasks. It is not specifically tailored for geospatial analysis or remote sensing applications.
Geospatial Capabilities:

Erdas Imagine: Erdas Imagine is specifically developed for geospatial data processing and offers advanced features for working with remote sensing imagery, such as radiometric correction, spectral analysis, and image interpretation. It also provides tools for georeferencing, mosaicking, and terrain analysis.
OpenCV: OpenCV does not have built-in geospatial capabilities. While it provides basic image processing functions that can be useful for geospatial tasks, it does not have specific tools for handling geospatial data formats, coordinate systems, or georeferencing.
Remote Sensing Workflows:

Erdas Imagine: Erdas Imagine provides comprehensive workflows and tools for remote sensing tasks, including image preprocessing, classification, feature extraction, and change detection. It supports various remote sensing data formats and integrates well with other geospatial software and data sources.
OpenCV: OpenCV does not have specialized workflows for remote sensing tasks. It focuses more on general computer vision algorithms and does not have specific functionalities tailored to the unique requirements of remote sensing workflows.
User Interface:

Erdas Imagine: Erdas Imagine provides a user-friendly graphical user interface (GUI) that allows users to access and utilize its extensive capabilities through an intuitive interface. It offers interactive tools and visualization options for geospatial data analysis and processing.
OpenCV: OpenCV primarily provides a library of functions and does not include a GUI. It is designed to be used programmatically, requiring developers to write code and integrate OpenCV functions into their own applications or scripts.
Industry Adoption:

Erdas Imagine: Erdas Imagine is widely used in industries such as remote sensing, environmental monitoring, agriculture, and natural resource management. It is recognized as a leading software in the field of geospatial analysis and remote sensing.
OpenCV: OpenCV is widely adopted in computer vision research, robotics, automation, and general-purpose image processing applications. It has a broad user base across various industries and academic fields.
In summary, while both Erdas Imagine and OpenCV provide image processing capabilities, Erdas Imagine is specifically designed for geospatial analysis, remote sensing, and handling geospatial data. It offers specialized tools, workflows, and integration with other geospatial software. On the other hand, OpenCV is a more general-purpose computer vision library that provides a broad range of image processing functions but does not have specialized geospatial features or workflows.

## OpenCV vs Global Mapper:
Application Focus:

Global Mapper: Global Mapper is a geospatial program designed specifically for working with geospatial data, including aerial imagery, LiDAR data, and vector data. It offers a wide range of tools and functionalities for geospatial analysis, data visualization, terrain modeling, and data conversion.
OpenCV: OpenCV is a versatile computer vision library that provides a broad set of functions and algorithms for general-purpose image and video processing, as well as computer vision tasks. It is not specifically tailored for geospatial analysis or data management.
Geospatial Capabilities:

Global Mapper: Global Mapper has specialized geospatial capabilities, such as terrain analysis, contour generation, orthophoto creation, and spatial querying. It supports a wide range of geospatial data formats and provides tools for data visualization, editing, and analysis specific to geospatial data.
OpenCV: OpenCV does not have built-in geospatial capabilities. While it provides basic image processing functions that can be useful for geospatial tasks, it does not have specific tools for handling geospatial data formats, coordinate systems, or specialized geospatial analysis.
Data Format Support:

Global Mapper: Global Mapper supports a wide range of geospatial data formats, including popular GIS formats such as ESRI Shapefile, GeoTIFF, KML/KMZ, and many others. It provides robust data import and export capabilities for seamless interoperability with different data sources.
OpenCV: OpenCV does not have built-in support for geospatial data formats. It primarily focuses on image and video processing, and while it provides functions for reading and writing image files, it lacks specialized support for geospatial data formats commonly used in GIS applications.
User Interface:

Global Mapper: Global Mapper provides a user-friendly graphical user interface (GUI) that allows users to interactively work with geospatial data. It offers intuitive tools, menus, and data visualization options for exploring, analyzing, and editing geospatial data.
OpenCV: OpenCV primarily provides a library of functions and does not include a GUI. It is designed to be used programmatically, requiring developers to write code and integrate OpenCV functions into their own applications or scripts.
Industry Adoption:

Global Mapper: Global Mapper is widely used in industries such as surveying, mapping, environmental planning, forestry, and natural resource management. It is recognized as a comprehensive geospatial software with a strong user base in various industries.
OpenCV: OpenCV is widely adopted in computer vision research, robotics, automation, and general-purpose image processing applications. It has a broad user base across various industries and academic fields.

In summary, Global Mapper is a specialized geospatial program that focuses on geospatial data analysis, visualization, and management. It provides tools and functionalities specific to geospatial data formats and workflows. OpenCV, on the other hand, is a general-purpose computer vision library that offers a wide range of functions for image and video processing tasks but does not have specialized geospatial features or workflows.

## In summary
We have same problem with all of instruments thay are not allowed using npm and some of them need to be paid and also some of them work only if you have internet
