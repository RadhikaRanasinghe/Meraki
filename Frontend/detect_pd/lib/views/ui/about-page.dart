import 'package:detect_pd/views/ui/settings-page.dart';
import 'package:detect_pd/views/widgets/navbar.dart';
import 'package:flutter/material.dart';
import 'package:detect_pd/views/ui/main.dart';
import 'package:detect_pd/views/widgets/home-Foreground.dart';
import 'package:detect_pd/views/widgets/home-background.dart';

// void main() {
//   runApp(MaterialApp(
//       home: AboutPDPage(),
//       theme: ThemeData(
//         canvasColor: Color.fromRGBO(118, 176, 195, 100),
//       )
//   ));
// }

class AboutPDPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HomeForeground(
        expandedHeight: 153.0,
        appBarChild: HomeBackground(
          title: 'About PD',
          logoPath: 'assets/pd_log_bg_small.png',
          height: 153.0,
          bigSquareColor: Color.fromRGBO(22, 111, 123, 100),
          smallSquareColor: Color.fromRGBO(169, 229, 238, 30),
          backgroundColor: Color.fromRGBO(94, 163, 184, 100),
          titleColor: Colors.white,
        ),
        appBarBackgroundColor:Color.fromRGBO(118, 176, 195, 100),
        fillChild: AboutPD(
          description: "Parkinson's Disease \n\nLorem Ipsum is simply dummy "
              "text of the printing and typesetting industry. Would you "
              "like to take the guided test or continue? \n\nLorem Ipsum is "
              "simply dummy text of the printing and typesetting industry."
              "Would you like to take the guided test or continue?",
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