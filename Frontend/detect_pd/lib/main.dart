import 'package:detect_pd/splash-screen.dart';
import 'package:detect_pd/widgets/home-buttons.dart';
import 'package:detect_pd/widgets/Settings.dart';
import 'package:detect_pd/widgets/home-background.dart';
import 'package:detect_pd/widgets/navbar.dart';
import 'package:detect_pd/settings-page.dart';
import 'package:flutter/material.dart';
import 'FAQ-Page.dart';
import 'package:detect_pd/widgets/home-Foreground.dart';

import 'about-page.dart';

void main() {
  runApp(MaterialApp(
    initialRoute:'load' ,
      routes:{
      'load':(context) =>SplashScreen(),
      },
      // home: HomePage(),
    debugShowCheckedModeBanner: false,
  ));
}

class HomePage extends StatelessWidget {
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
        ),
        appBarBackgroundColor: Color.fromRGBO(94, 163, 184, 100),
        fillChild: NewSquare(),
        fillColor:  Color.fromRGBO(240, 241, 226, 100),
      ),
      bottomNavigationBar: NavBar(
        link1: (){
          Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (context) => AboutPDPage()));
        },
        link2: null,
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