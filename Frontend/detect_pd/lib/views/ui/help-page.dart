import 'package:detect_pd/utils/url-launcher.dart';
import 'package:detect_pd/views/ui/settings-page.dart';
import 'package:detect_pd/views/widgets/home-background.dart';
import 'package:detect_pd/views/widgets/navbar.dart';
import 'package:flutter/material.dart';
import 'package:detect_pd/views/widgets/home-foreground.dart';
import 'package:detect_pd/main.dart';

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
          backgroundColor: Colors.transparent,
          titleColor: Colors.white,
        ),  //HomeBackground
        appBarBackgroundColor:Colors.transparent,
        fillChild: AboutPD(
          description: "Step 1 : Download the template from Home page\n\n"
              "Step 2 : Print and trace on the template\n\n"
              "Step 3 : Fill out form details\n\n"
              "Step 4 : Upload photo of the traced template\n\n"
              "Step 5 : Check the result\n\n",
          fontSize: 17.0,
          alignment: Alignment.topCenter,
          textColor: Colors.white,
        ),  //AboutPD
        fillColor:  BoxDecoration(
          // color: fillColor,
            gradient: new LinearGradient(
              colors: [
                const Color(0xFF0277BD),
                Color.fromRGBO(22, 111, 123, 100)
              ],
              begin: const FractionalOffset(0.0, 0.0),
              end:const FractionalOffset(1.0, 0.0),
            ),
            borderRadius: new BorderRadius.only(
              topLeft: const Radius.circular(40.0),
              topRight: const Radius.circular(40.0),
            )
        ),
      ),// HomeForeground
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
        backgroundColor: Colors.transparent ,
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
              height: 1.5, // the height between text, default is null
              letterSpacing: 1.0
          ),  // TextStyle
        ),  // Text
        margin: EdgeInsets.all(30.0),
        padding: EdgeInsets.all(10.0),
        alignment: alignment,
      ),  // Container
    );  // Center
  }
}