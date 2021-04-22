#include <stdio.h>
#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>

#include <stdlib.h>
//#include <math.h>
#include <vector>
#include <list>
#define pb push_back
#define rb pop_back 
#define DISPLACEMENT 10


using namespace cv;
using namespace std;

struct cpoint{
	int x,y;
	cpoint(){};
	cpoint(int x, int y):
	x(x), y(y) {};
};

Mat img;
//Functions to recovery the Neighboors as follow:		
// P9 P2 P3
// P8 P1 P4
// P7 P6 P5
int P1(Mat dest, int line, int col)
{
    return dest.at<uchar>(line, col);
}

int P2(Mat dest, int line, int col)
{
    return dest.at<uchar>(line-1, col);
}

int P3(Mat dest, int line, int col)
{
    return dest.at<uchar>(line-1, col+1);
}

int P4(Mat dest, int line, int col)
{
    return dest.at<uchar>(line, col+1);
}

int P5(Mat dest, int line, int col)
{
    return dest.at<uchar>(line+1, col+1);
}

int P6(Mat dest, int line, int col)
{
    return dest.at<uchar>(line+1, col);
}

int P7(Mat dest, int line, int col)
{
    return dest.at<uchar>(line+1, col-1);
}

int P8(Mat dest, int line, int col)
{
    return dest.at<uchar>(line, col-1);
}

int P9(Mat dest, int line, int col)
{
    return dest.at<uchar>(line-1, col-1);
}

void Delete(Mat dest, int line, int col)
{
    dest.at<uchar>(line, col) = 0;
}

void Zhang_Suen(Mat dest)
{
    int height = dest.rows;
    int width = dest.cols;						
    bool ThiningContinue = true;
    int line, col;
    cpoint ActualPixel;
    int Conectivity = 0, Neighboors = 0;
    list<cpoint> RemPoints;
    list<cpoint>::iterator it;

    for (line = 0; line < height; line++)
        for (col = 0; col < width; col++)
        {
            dest.at<uchar>(line, col) = dest.at<uchar>(line, col) == 255?0:1;
        }

    while (ThiningContinue)
    {
        ThiningContinue = false;

        // First Sub-Iteraction
        for (line = 1; line < height - 1; line++)
        {
            for (col = 1; col < width - 1; col++)
            {
                Neighboors = 0;
                Conectivity = 0;
                // Pixel must be black
                if (P1(dest, line, col) == 0)
                    continue;
                // Connectivity number must be 1;
                Conectivity = (P2(dest, line, col) == 0 && P3(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P3(dest, line, col) == 0 && P4(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P4(dest, line, col) == 0 && P5(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P5(dest, line, col) == 0 && P6(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P6(dest, line, col) == 0 && P7(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P7(dest, line, col) == 0 && P8(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P8(dest, line, col) == 0 && P9(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P9(dest, line, col) == 0 && P2(dest, line, col) == 1) ? 1 : 0;
                if (Conectivity != 1)
                    continue;
                // 2 <= BlackNeighboors <= 6
                Neighboors = P2(dest, line, col) + P3(dest,line, col) +
                    P4(dest, line, col) + P5(dest, line, col) +
                    P6(dest, line, col) + P7(dest, line, col) +
                    P8(dest, line, col) + P9(dest, line, col);
                if (Neighboors < 2 || Neighboors > 6)
                    continue;
                // At least one of P2, P4 and P8 are background
                Neighboors = 0;
                Neighboors = P2(dest, line, col) * P4(dest, line, col) * P8(dest, line, col);
                if (Neighboors != 0)
                    continue;

                // At least one of P2, P6 and P8 are background
                Neighboors = 0;
                Neighboors = P2(dest, line, col) * P6(dest, line, col) * P8(dest, line, col);
                if (Neighboors != 0)
                    continue;
                // Actual Pixel was deleted
                ThiningContinue = true;
                RemPoints.push_back(cpoint(line, col));
            }
        }
        for (it = RemPoints.begin(); it != RemPoints.end(); it++)
            dest.at<uchar>((*it).x, (*it).y) = 0;
        RemPoints.clear();
        // Second Sub-Iteraction
        for (line = 1; line < height - 1; line++)
        {
            for (col = 1; col < (int)width - 1; col++)
            {
                Neighboors = 0;
                Conectivity = 0;
                // Pixel must be black
                if (P1(dest, line, col) == 0)
                    continue;
                // Connectivity number must be 1;
                Conectivity = (P2(dest, line, col) == 0 && P3(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P3(dest, line, col) == 0 && P4(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P4(dest, line, col) == 0 && P5(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P5(dest, line, col) == 0 && P6(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P6(dest, line, col) == 0 && P7(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P7(dest, line, col) == 0 && P8(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P8(dest, line, col) == 0 && P9(dest, line, col) == 1) ? 1 : 0;
                Conectivity += (P9(dest, line, col) == 0 && P2(dest, line, col) == 1) ? 1 : 0;
                if (Conectivity != 1)
                    continue;
                // 2 <= BlackNeighboors <= 6
                Neighboors = P2(dest, line, col) + P3(dest, line, col) +
                    P4(dest, line, col) + P5(dest, line, col) +
                    P6(dest, line, col) + P7(dest, line, col) +
                    P8(dest, line, col) + P9(dest, line, col);
                if (Neighboors < 2 || Neighboors > 6)
                    continue;
                // At least one of P2, P4 and P6 are background
                Neighboors = 0;
                Neighboors = P2(dest, line, col) * P4(dest, line, col) * P6(dest, line, col);
                if (Neighboors != 0)
                    continue;
                // At least one of P2, P6 and P8 are background
                Neighboors = 0;
                Neighboors = P4(dest, line, col) * P6(dest, line, col) * P8(dest, line, col);
                if (Neighboors != 0)
                    continue;
                // Actual Pixel was deleted
                ThiningContinue = true;
                RemPoints.push_back(cpoint(line, col));
            }
        }
        for (it = RemPoints.begin(); it != RemPoints.end(); it++)
            dest.at<uchar>((*it).x, (*it).y) = 0;
        RemPoints.clear();
    }
    for (line = 0; line < height; line++)
    {
        for (col = 0; col < width; col++)
        {
            if (P1(dest, line, col) == 0)
                dest.at<uchar>(line, col) = 255;
            else
                dest.at<uchar>(line, col) = 0;
        }
    }
}

struct vertex
{
	double x,y;
};

typedef struct vertex Vertices;

struct radius_angle
{
	double radius, angle;
};
typedef struct radius_angle RadiusAngle;


void invert(double *ini, double *fim)
{
	double i,f;
	i=*ini;
	f=*fim;
	*ini=f;
	*fim=i;
}

void lineIDDA(Mat img_, double yi, double xi, double yf, double xf, vector<Vertices> &v)
{
	int x,y,deltax,deltay,erro=0,q=0,quant;
	deltax=xf-xi;
	deltay=yf-yi;
	Vertices vert;
	// When yi>yf the line is diagonal to down. For this is
	// necessary invert the points
	// When Deltax= 0 and Deltay  < 0, the line is in vertical
	// to down. For this is necessary invert yi with yf.
	if ((yi>yf) || ((deltax==0) && (deltay<0)))
	{
		invert(&xi,&xf);
		invert(&yi,&yf);
		deltax=xf-xi;
		deltay=yf-yi;
	}
	x=xi;
	y=yi;

	// "quant" denotes the maximum number of ploted points
	if (abs(deltax)>abs(deltay))
		quant=abs(deltax);
	else
		quant=abs(deltay);
	bool get_point = true;
	bool entered = false;
	bool finished = false;
	int walk = 1000;//clean more pixels.
	while (q<=quant && walk) //While have points to plot
	{
		if (x>=0 && y>=0 && x<img_.cols && y< img_.rows)
		{
			if(!entered && img_.at<uchar>(y, x) == 0)//Find a espiral
			{
				entered = true;
				if(get_point)//get the first point.
				{
					get_point = false;
					vert.x = x;
					vert.y = y;
					v.pb(vert);
				}
				img_.at<uchar>(y, x) = 255;//Set the color white to avoid reprocessing
			}
		}

		if(entered){
			walk--;
			if (x>=0 && y>=0 && x<img_.cols && y<img_.rows)
			   img_.at<uchar>(y, x) = 255;//Set the color white to avoid reprocessing
		}

		
		if ((deltax>=0) && (deltay>=0) && (deltax>=deltay))// 1 oct
		{
			if ((erro<0) || (deltay==0))
			{
				x++;
				erro=erro+deltay;
			}
			else
			{
				x++;
				y++;
				erro=erro+deltay-deltax;
			}
		}
		else
		if ((deltax>=0) && (deltay>=0) && (deltay>deltax))// 2 oct
		{
			if (erro<0)
			{
				x++;
				y++;
				erro=erro+deltay-deltax;
			}
			else
			{
				y++;
				erro=erro-deltax;
			}
		}
		else
		if ((deltay>=0) && (deltax<0) && (-deltax>=deltay)) // 4 oct
		{
			if ((erro<0) || (deltay==0))
			{
				x--;
				erro=erro+deltay;
			}
			else
			{
				x--;
				y++;
				erro=erro+deltax+deltay;
			}
		}
		else
		if ((deltay>0) && (deltax<0) && (deltay>-deltax)) // 3 oct
		{
			if (erro<0)
			{
				x--;
				y++;
				erro=erro+deltax+deltay;
			}
			else
			{
				y++;
				erro=erro+deltax;
			}
		}
		else
		if ((deltax>=0) && (deltay<0) && (deltax>=-deltay))// 8 oct
		{
			if ((erro<0))
			{
				x++;
				erro=erro-deltay;
			}
			else
			{
				x++;
				y--;
				erro=erro+abs(deltay)-deltax;
			}
		}
		else
		if ((deltax>=0) && (deltay<0) && (-deltay>deltax))// 7 oct
		{
			if (erro<0)
			{
				x++;
				y--;
				erro=erro-deltay-deltax;
			}
			else
			{
				y--;
				erro=erro-deltax;
			}
		}
		else
		if ((deltay<0) && (deltax<0) && (-deltay>-deltax)) // 3 oct
		{
			if (erro<0)
			{
				x--;
				y--;
				erro=erro+deltax-deltay;
			}
			else
			{
				y--;
				erro=erro+deltax;
			}
		}
		else
		if ((deltay<0) && (deltax<0) && (-deltax>=-deltay)) // 4 oct
		{
			if ((erro<0))
			{
				x--;
				erro=erro-deltay;
			}
			else
			{
				x--;
				y--;
				erro=erro+deltax-deltay;
			}
		}
		q++; //number of plotted points
	}
}

//---------------------------------------------------------------------------
void rotation(Vertices *vert, int yp, int xp, int teta)
{
	double x,y;
	x=(double)((((*vert).x-xp)*cos(teta*3.14159265358/180))-(((*vert).y-yp)*sin(teta*3.14159265358/180)))+xp;
	y=(double)((((*vert).x-xp)*sin(teta*3.14159265358/180))+(((*vert).y-yp)*cos(teta*3.14159265358/180)))+yp;
	(*vert).x=x;
	(*vert).y=y;
}

//VERIFY THE CENTRAL PÍXEL
bool verify(Mat img_, int y, int x)
{
	int cont = 0;
	for(int i = y-1; i < y+2; i++)
		for(int j = x-1; j < x+2; j++)
			if(img_.at<uchar>(i, j)==0)
				cont++;
	return cont==2;
}

//FIND THE SPIRAL ORIGEN
void origem(Mat img_, int *oy, int *ox)
{
	int lines = (*oy)+100, cols= (*ox)+100, i, j;
	int com_line = (*oy)-100, com_col = (*ox)-100;

	for(i = com_line; i < lines; i++)
	{
		for(j = com_col; j < cols; j++)
		{
			if(img_.at<uchar>(i, j)==0)
			{
				if(verify(img_, i, j))
				{
					*ox = j;
					*oy = i;
				}
			}
		}
	}
}

int main(int argc,char* argv[])
{
	vector<RadiusAngle> radiusangle, radiusrigin, difradial;
	vector<Vertices> ptosoriginal, ptosdesenhada, tremor_relativo;
	vector<double> tremor;
	RadiusAngle ra, raorigin;
	double raiz, atangente;
	Vertices vert;
	
	if ( argc != 4 )
    {
        printf("\n*** Given an exam image and the pen image save the features extracted in the file <RMS.txt> \n\n");
        printf("\n*** usage: extractFeats <name_of_input_image_with_extension> <class_type -- 'c' to control and 'p' to patient>\n");
        printf("\n*** Incorrect number of input parameters!\n");    
        return -1;
    }
	img = imread(argv[1], CV_LOAD_IMAGE_COLOR);
	Mat img1 = imread(argv[2], CV_LOAD_IMAGE_COLOR);    
	
	//Gray scale
	Mat img_ = Mat(Size(img.cols, img.rows),CV_8UC1); 
	cvtColor(img, img_, CV_BGR2GRAY);
	threshold(img_, img_, 220, 255, 0);
	Zhang_Suen(img_);

	
	//Spiral pen
	Mat img1_ = Mat(Size(img.cols, img.rows),CV_8UC1); 
	
	int nx = img.cols, //number of collumns
        ny = img.rows; //number of lines/rows
        int x,y,z;
   
	cvtColor(img1, img1_, CV_BGR2GRAY);
	threshold(img1_, img1_, 220, 255, 0);
	Zhang_Suen(img1_);
	
	int yc = img_.rows/2;//370;//
	int xc = img_.cols/2;//350;//
	//Find the spiral origin.
	origem(img1_, &yc, &xc);	
	
	/////////////////////////////////////////////////////////////////////////
	//Get points from spiral
	for(int j = 0; j < 3; j++)//3 turns in the spiral.
	{
	   vert.y=yc;
	   vert.x=img_.cols+350;//pegar a img inteira.
	   rotation(&vert, yc, xc, 1);
	   for (int i=0; i<360; i++)
	   {
	       int pt_ori = ptosoriginal.size();
	       int pt_des = ptosdesenhada.size();
	       rotation(&vert, yc, xc, -1);
	       lineIDDA(img1_, yc, xc, vert.y, vert.x, ptosoriginal);
	       lineIDDA(img_, yc, xc, vert.y, vert.x, ptosdesenhada);
	   }
	}
	////////////////////////////////////////////////////////////////////////
	yc = img_.rows/2;//370;//
	xc = img_.cols/2;//350;//
	
	//////////////////////////////////////////////////////////////////////
    // Transformation to polar coordinates
    for(int i = 0; i < ptosoriginal.size(); i++)
	{
	    raiz = (ptosoriginal[i].x-xc)*(ptosoriginal[i].x-xc) + (ptosoriginal[i].y-yc)*(ptosoriginal[i].y-yc);
	    raorigin.radius = sqrt(raiz);//computating the radius.
	    atangente = (ptosoriginal[i].y-yc)/(ptosoriginal[i].x-xc);
	    raorigin.angle = atan(atangente);//computating the angle. (Radianos)
	    radiusrigin.pb(raorigin); 
	}
	
	for(int i = 0; i < ptosdesenhada.size() && i < ptosoriginal.size(); i++)
	{
	    raiz = (ptosdesenhada[i].x-xc)*(ptosdesenhada[i].x-xc) + (ptosdesenhada[i].y-yc)*(ptosdesenhada[i].y-yc);
	    ra.radius = sqrt(raiz);
	    atangente = (ptosdesenhada[i].y-yc)/(ptosdesenhada[i].x-xc);
	    ra.angle = atan(atangente);
	    radiusangle.pb(ra); 	
	}
	/////////////////////////////////////////////////////////////////////
	//Calculate the difference between the template and drawed spiral
	double dif_rad = 0.0, 
	       prev_rad = radiusrigin[0].radius - radiusangle[0].radius;
	int count_cross = 0;       
	
	
	ra.radius = abs(prev_rad);       
	difradial.pb(ra);
	
	for(int i = 1; i < ptosdesenhada.size() && i < ptosoriginal.size(); i++)
	{
	    dif_rad = radiusrigin[i].radius - radiusangle[i].radius;
	    ra.radius = abs(dif_rad);       
	    difradial.pb(ra);
	    if(dif_rad * prev_rad < 0) count_cross++; //CROSS THE TEMPLATE
	    prev_rad = dif_rad;
	}
	/////////////////////////////////////////////////////////////////////
	//computating the Relative Tremor
	for(int i = 0; i < ptosdesenhada.size() && i < ptosoriginal.size(); i++)
	{
		raiz = (ptosoriginal[i].x-xc)*(ptosoriginal[i].x-xc) + (ptosoriginal[i].y-yc)*(ptosoriginal[i].y-yc);
		vert.x = (1 - difradial[i].radius / sqrt(raiz)) * ptosdesenhada[i].x;
		//cout << vert.x << endl;
		vert.y = (1 - difradial[i].radius / sqrt(raiz)) * ptosdesenhada[i].y;
		//cout << vert.y << endl;
		tremor_relativo.pb(vert);
	}
	
	double mean_tremor = 0.0;
	double std_tremor = 0.0;
	double max_tremor = 0.0;
	double min_tremor = 10000.0;
	int count = 0;
	
	for(int i = 0; i < ptosdesenhada.size() && i < ptosoriginal.size(); i++)
	{
		raiz = sqrt( (ptosoriginal[i].x-xc)*(ptosoriginal[i].x-xc) + (ptosoriginal[i].y-yc)*(ptosoriginal[i].y-yc) );
		tremor.pb(raiz);
	}	
	
	for(int i = DISPLACEMENT; i < tremor.size(); i++)
	{
	        double dif = fabs(tremor[i] - tremor[i-DISPLACEMENT]);
		mean_tremor += dif;
		count++;
		if(dif > max_tremor) max_tremor = dif;
		if(dif < min_tremor) min_tremor = dif;		
	}
	mean_tremor /= (double)count;
	
	for(int i = DISPLACEMENT; i < tremor.size(); i++)
	{
	        double dif = fabs(tremor[i] - tremor[i-DISPLACEMENT]);
		std_tremor += pow(dif - mean_tremor,2.0) / (double)(tremor.size()-DISPLACEMENT);
		
	}
	
	
	///////// Extracting features from Tremor //////////
	//computating the RMS (Root Mean Square)
	double RMS = 0.0;
	double minRMS = 10e10, maxRMS = 0.0;
	double std = 0.0;
	int min_p = ptosdesenhada.size();
	if(min_p > ptosoriginal.size() )
	   min_p = ptosoriginal.size();
	for(int i = 0; i < ptosdesenhada.size() && i < ptosoriginal.size(); i++)
	{
		RMS += difradial[i].radius * difradial[i].radius;
		if(difradial[i].radius * difradial[i].radius > maxRMS) maxRMS = difradial[i].radius * difradial[i].radius;
		if(difradial[i].radius * difradial[i].radius < minRMS) minRMS = difradial[i].radius * difradial[i].radius;
		
	}
	
	RMS /= (double)min_p;
	for(int i = 0; i < ptosdesenhada.size() && i < ptosoriginal.size(); i++)
	{
		std += pow(difradial[i].radius * difradial[i].radius - RMS,2.0) / (double)ptosoriginal.size();				
	}
	
	std = sqrt(std);
	
	fprintf(stderr,"\n[%s : %s] RMS: %lf (+/- %lf) \t maxRMS: %lf \t minRMS: %lf Npoints: %d: %d \nMT:%lf Max:%lf Min: %lf Std:%lf Cross:%lf ",argv[1], argv[2], RMS, std, maxRMS, minRMS, (int)ptosdesenhada.size(), (int)ptosoriginal.size(), mean_tremor, max_tremor, min_tremor, std_tremor, ((double)count_cross)/(double)count);
	FILE *f = fopen("RMS.txt","a");
	int class_img;
	if(argv[3][0] == 'c') class_img = 1;
    else
        if(argv[3][0] == 'p') class_img = 2;
        else
        {
            fprintf(stderr,"\nERROR: unknown class. The class identifier needs to be 'c'(control) or 'p'(patient)\n ");
            exit(1);
        }
	fprintf(f,"%+d 1:%lf 2:%lf 3:%lf 4:%lf 5:%lf 6:%lf 7:%lf 8:%lf 9:%lf\n",class_img, RMS, std, maxRMS, minRMS, mean_tremor, max_tremor, min_tremor, std_tremor, ((double)count_cross)/(double)count);
	fclose(f);
}
