import 'package:detect_pd/utils/url-launcher.dart';
import 'package:detect_pd/views/ui/splash-screen.dart';
import 'package:detect_pd/views/widgets/home-buttons.dart';
import 'package:detect_pd/views/widgets/home-background.dart';
import 'package:detect_pd/views/widgets/navbar.dart';
import 'package:detect_pd/views/ui/settings-page.dart';
import 'package:flutter/material.dart';
import 'package:showcaseview/showcase_widget.dart';
import 'package:detect_pd/views/widgets/home-foreground.dart';
import 'package:detect_pd/views/ui/answer-page.dart';

void main() {
  runApp(MaterialApp(

    initialRoute:'load' ,
      routes:{
      'load':(context) =>SplashScreen(),
        '/answers-page':(context) => AnswerPage(),
      },
    debugShowCheckedModeBanner: false,
  )); // MaterialApp
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
        ), // HomeBackground
        appBarBackgroundColor: Color.fromRGBO(94, 163, 184, 100),
        fillChild: ShowCaseWidget(builder: Builder(builder: (_) => NewSqaure())),
        fillColor:  Color.fromRGBO(240, 241, 226, 100),
      ), // HomeForeground
      bottomNavigationBar: NavBar(
        link1: launcher,
        link2: null,
        link3: (){
          Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (context) => SettingsPage()));
        },
        backgroundColor: Color.fromRGBO(240, 241, 226, 100) ,
      ), // NavBar
    ); // Scaffold
  }
}