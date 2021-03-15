#include <stdio.h>
#include <opencv2/opencv.hpp>

#define BLUR_RADIUS 5

using namespace cv;

/* Method for remove the pen and background and maintains just the template
 * of a parkison image test (spiral or meander) 
 */
int main(int argc, char** argv )
{
  
    char file_name[100];
    sprintf(file_name,"%s.jpg",argv[1]);      
    if ( argc != 2 )
    {
        printf("\n*** Given an exam image return the Template image\n");        
        printf("\n*** usage: extractTemplate <name_of_input_image_without_extension>\n");
        printf("\n*** Incorrect number of input parameters!\n");   
        return -1;
    }

    Mat img,img_gray;
    img = imread(file_name,1 );
    blur(img,img,Size(BLUR_RADIUS, BLUR_RADIUS) );
    
    if (!img.data)
    {
        printf("No image data %s\n",argv[1]);
        return -1;
    }
    
    int nx = img.cols, //number of collumns
        ny = img.rows; //number of lines/rows
    int x,y,z;
   
    
  
    for(y = 0; y < ny; y++)
    {
		for(x = 0; x < nx; x++)
		{
	
	      Vec3b color = img.at<Vec3b>(Point(x,y));
	
          if((color[0] < 120 && color[1] < 120 && color[2] < 120))
	      {	
			img.at<Vec3b>(Point(x, y))[0] = 0;
			img.at<Vec3b>(Point(x, y))[1] = 0;
			img.at<Vec3b>(Point(x, y))[2] = 0;			      	      
	      }
	      else
	      {
			img.at<Vec3b>(Point(x, y))[0] = 255;
			img.at<Vec3b>(Point(x, y))[1] = 255;
			img.at<Vec3b>(Point(x, y))[2] = 255;			      	      
	      }	  
	     
		}	
    }
    int erosion_type =  MORPH_RECT;// MORPH_RECT; //MORPH_ELLIPSE; // MORPH_RECT; // MORPH_CROSS;
    int erosion_size = 2;
    Mat element = getStructuringElement( erosion_type,
                                       Size( 2*erosion_size + 1, 2*erosion_size+1 ),
                                       Point( erosion_size, erosion_size ) );
  
    erode( img, img, element );

    // Apply the dilate and erosin operations to remove noise and debris in the scanned image
    erosion_size = 1;
    Mat element1 = getStructuringElement( erosion_type,
                                       Size( 2*erosion_size + 1, 2*erosion_size+1 ),
                                       Point( erosion_size, erosion_size ) );
   dilate( img, img, element1 );
   dilate( img, img, element1 );
  
  
  sprintf(file_name,"%s_template.jpg",argv[1]);    
  blur(img,img,Size(3*BLUR_RADIUS, 3*BLUR_RADIUS) );
  cvtColor( img, img_gray, CV_BGR2GRAY );
  
  Mat element2 = getStructuringElement( erosion_type,
                                       Size( 2*erosion_size + 1, 2*erosion_size+1 ),
                                       Point( erosion_size, erosion_size ) );
  
  //Otsu threshold is used to remove the noise and background
  cv::threshold(img_gray, img_gray, 0, 255, CV_THRESH_BINARY | CV_THRESH_OTSU);
  dilate( img_gray, img_gray, element2 );
  dilate( img_gray, img_gray, element2 );
  erode( img_gray, img_gray, element2 );
  erode( img_gray, img_gray, element2 );
  erode( img_gray, img_gray, element2 );
  imwrite(file_name,img_gray);

  

  return 0;
}
