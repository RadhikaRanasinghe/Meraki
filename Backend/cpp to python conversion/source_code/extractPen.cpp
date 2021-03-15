#include <stdio.h>
#include <opencv2/opencv.hpp>

#define BLUR_RADIUS 5

using namespace cv;

/* Method for remove the template and background and maintains just the pen
 * of a parkison image test (spiral or meander) 
 */

int main(int argc, char** argv )
{
  
    char file_name[100];
    sprintf(file_name,"%s.jpg",argv[1]);      
    if ( argc != 2 )
    {
        printf("\n*** Given an exam image return the Pen image\n");
        printf("\n*** usage: extractPen <name_of_input_image_without_extension>\n");
        printf("\n*** Incorrect number of input parameters!\n");    
        return -1;
    }

    Mat img, img_gray;
    img = imread(file_name, 1 );
    blur(img,img,Size(BLUR_RADIUS,BLUR_RADIUS) );
    medianBlur(img,img,11);
    
    if ( !img.data )
    {
        printf("No image data \n");
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
	      
	      
	      if((color[0] > 200 && color[1] > 200 && color[2] > 200) || color[0] < 70)
	      {	
			img.at<Vec3b>(Point(x, y))[0] = 255;
			img.at<Vec3b>(Point(x, y))[1] = 255;
			img.at<Vec3b>(Point(x, y))[2] = 255;			      	      
	      }
	     
		}	
    }
    
    
    int erosion_type =   MORPH_RECT; //MORPH_ELLIPSE; // MORPH_RECT; // MORPH_CROSS;
    int erosion_size = 1;
    Mat element = getStructuringElement( erosion_type,
                                       Size( 2*erosion_size + 1, 2*erosion_size+1 ),
                                       Point( erosion_size, erosion_size ) );
  
  dilate( img, img, element );
  dilate( img, img, element );
  
  erosion_size = 2;
  Mat element1 = getStructuringElement( erosion_type,
                                       Size( 2*erosion_size + 1, 2*erosion_size+1 ),
                                       Point( erosion_size, erosion_size ) );
  erode( img, img, element1 );
  
  
  for(y = 0; y < ny; y++)
  {
	for(x = 0; x < nx; x++)
	{
	      Vec3b color = img.at<Vec3b>(Point(x,y));
	      int difRG = abs(color[0] - color[1]);
	      int difRB = abs(color[0] - color[2]);
	      int difGB = abs(color[1] - color[2]);
 	      if(difGB < 30 && difRB < 30 && difRG < 40)
	      {	
            img.at<Vec3b>(Point(x, y))[0] = 255;
            img.at<Vec3b>(Point(x, y))[1] = 255;
            img.at<Vec3b>(Point(x, y))[2] = 255;			      	      
	      }	
	}	
  }
  
  
  sprintf(file_name,"%s_pen.jpg",argv[1]);    
  blur(img,img,Size(BLUR_RADIUS,BLUR_RADIUS) );
  medianBlur(img,img,3);
  imwrite(file_name,img);
  

  
  return 0;
}
