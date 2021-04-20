import 'package:detect_pd/views/widgets/home-background.dart';
import 'package:flutter/material.dart';
import 'package:detect_pd/views/widgets/home-foreground.dart';
import 'package:detect_pd/views/ui/gallery-form-page.dart';
import 'package:detect_pd/main.dart';

void main() {
  runApp(MaterialApp(
    home: ErrorPage(),
    debugShowCheckedModeBanner: false,
  )); // MaterialApp
}

class ErrorPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HomeForeground(
        expandedHeight: 153.0,
        appBarChild: HomeBackground(
          title: 'Home',
          logoPath: 'assets/pd_log_bg_small.png',
          height: 153.0,
          bigSquareColor: Color.fromRGBO(22, 111, 123, 100),
          smallSquareColor: Color.fromRGBO(169, 229, 238, 30),
          backgroundColor: Color.fromRGBO(94, 163, 184, 100),
          titleColor: Colors.white,
        ), // HomeBackground
        appBarBackgroundColor: Color.fromRGBO(94, 163, 184, 100),
        fillChild: ErrorForeground(
          errorMessage: "Unexpected error. Please resubmit the form.",
          padding: EdgeInsets.all(8.0),
          elevation: 5.0,
          fontSize: 15.0,
          width: 200.0,
          link1: (){
            Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => GalleryFormPage()));
          },
          link2: (){
            Navigator.pushReplacement(context,  MaterialPageRoute(builder: (context) => HomePage()));
          },
        ),
        fillColor:  Color.fromRGBO(240, 241, 226, 100),
      ), // HomeForeground
    ); // Scaffold
  }
}

class ErrorForeground extends StatelessWidget {
  final errorMessage;
  final width;
  final height;
  final padding;
  final elevation;
  final link1;
  final link2;
  final fontSize;

  const ErrorForeground({this.errorMessage, this.width, this.height, this.padding, this.elevation, this.fontSize, this.link1, this.link2});

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Center(
        child: Column(
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.fromLTRB(30.0, 50.0, 10.0, 50.0),
              child: Text(errorMessage,
              style: TextStyle(
                fontSize: 17.0,
                fontWeight: FontWeight.bold
                ),
              ),
            ),
            Container(
              width: width,
              height: height,
              // using the raised button widget with an icon
              child: RaisedButton.icon(
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(100),
                    side: BorderSide(color: Colors.grey, width: 1)
                ),  // RoundedRectangleBorder
                color: Colors.grey,
                icon: Icon(Icons.autorenew, color: Colors.black),
                label: Text("Resubmit",
                  style: TextStyle(
                      color: Colors.white70, fontSize: fontSize
                  ),  // TextStyle
                ),  // Text
                padding: padding,
                elevation: elevation,
                onPressed: link1,
              ),  // RaisedButton.icon
            ),
            Container(
              width: width,
              height: height,
              // using the raised button widget with an icon
              child: RaisedButton.icon(
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(100),
                    side: BorderSide(color: Colors.grey, width: 1)
                ),  // RoundedRectangleBorder
                color: Colors.grey,
                icon: Icon(Icons.cancel, color: Colors.black),
                label: Text("Cancel",
                  style: TextStyle(
                      color: Colors.white70, fontSize: fontSize
                  ),  // TextStyle
                ),  // Text
                padding: padding,
                elevation: elevation,
                onPressed: link2,
              ),  // RaisedButton.icon
            ),
          ],
        ),
      ),
    );
  }
}