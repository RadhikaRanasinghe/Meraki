import 'package:detect_pd/utils/url-launcher.dart';
import 'package:detect_pd/views/ui/settings-page.dart';
import 'package:detect_pd/views/widgets/home-background.dart';
import 'package:detect_pd/views/widgets/navbar.dart';
import 'package:flutter/material.dart';
import 'package:detect_pd/views/widgets/home-foreground.dart';
import 'package:detect_pd/views/ui/main.dart';

class HelpPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HomeForeground(
        expandedHeight: 153.0,
        appBarChild: HomeBackground(
          title: 'Help',
          logoPath: 'assets/pd_log_bg_small.png',
          height: 153.0,
          bigSquareColor: Color.fromRGBO(22, 111, 123, 100),
          smallSquareColor: Color.fromRGBO(169, 229, 238, 30),
          backgroundColor: Color.fromRGBO(94, 163, 184, 100),
          titleColor: Colors.white,
        ),  //HomeBackground
        appBarBackgroundColor:Color.fromRGBO(118, 176, 195, 100),
        fillChild: AboutPD(
          description: "Step 1 : Download the template from Home page\n\n\n"
              "Step 2 : Print and trace on the template\n\n\n"
              "Step 3 : Fill out form details\n\n\n"
              "Step 4 : Upload photo of the traced template\n\n\n"
              "Step 5 : Check the result\n\n\n",
          fontSize: 17.0,
          alignment: Alignment.topCenter,
          textColor: Colors.white,
        ),  //AboutPD
        fillColor:  Color(0xff033e6b),
      ),  // HomeForeground
      bottomNavigationBar: NavBar(
        link1: launcher,
        link2: (){
          Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (context) => HomePage()));
        },
        link3: (){
          Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (context) => SettingsPage()));
        },
        backgroundColor: Color.fromRGBO(240, 241, 226, 100) ,
      ),  // NavBar
    );  // Scaffold
  }
}

class AboutPD extends StatelessWidget {

  // creating the variables
  final description;
  final fontSize;
  final alignment;
  final textColor;

  // creating the constructor
  const AboutPD({this.description, this.fontSize, this.alignment, this.textColor});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        child: Text(description,
          style: TextStyle(
            color: textColor,
            fontSize: fontSize,
          ),  // TextStyle
        ),  // Text
        margin: EdgeInsets.all(30.0),
        padding: EdgeInsets.all(10.0),
        alignment: alignment,
      ),  // Container
    );  // Center
  }
}