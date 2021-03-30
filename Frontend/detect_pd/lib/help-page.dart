import 'package:detect_pd/settings-page.dart';
import 'package:detect_pd/widgets/home-background.dart';
import 'package:detect_pd/widgets/navbar.dart';
import 'package:flutter/material.dart';
import 'widgets/home-foreground.dart';
import 'main.dart';


void main() {
  runApp(MaterialApp(
      home: HelpPage(),
      // using a theme
      theme: ThemeData(
        canvasColor: Color.fromRGBO(118, 176, 195, 100),
      )
  ));
}

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
        ),
        appBarBackgroundColor:Color.fromRGBO(118, 176, 195, 100),
        fillChild: AboutPD(
          description: "Step 1 : Dummy Text\n\n\n "
              "Step 2: Dummy Text\n\n\n "
              "Step 3: Dummy Text\n\n\n"
              "Step 4: Dummy Text\n\n\n"
              "Step 5: Dummy Text\n\n\n",
          fontSize: 20.0,
          alignment: Alignment.topCenter,
          textColor: Colors.white,
        ),
        // fillColor:  Color.fromRGBO(240, 241, 226, 100),
        fillColor:  Color(0xff033e6b),
      ),
      bottomNavigationBar: NavBar(
        link1: null,
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
      ),
    );
  }
}

class AboutPD extends StatelessWidget {
  // creating the variables
  final description;
  final fontSize;
  final alignment;
  final textColor;

  const AboutPD({this.description, this.fontSize, this.alignment, this.textColor});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        child: Text(description,
          style: TextStyle(
            color: textColor,
            fontSize: fontSize,
          ),
        ),
        margin: EdgeInsets.all(30.0),
        padding: EdgeInsets.all(10.0),
        alignment: alignment,
      ),
    );
  }
}