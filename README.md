## Instruction
1. **node -v** need to be 16.18.0
2. npm install
3. create folder "uploads" in root folder near with "src"
4. npm run start:dev - to start server
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
 
