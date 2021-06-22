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
          backgroundColor: Colors.transparent,
          titleColor: Colors.white,
        ), // HomeBackground
        appBarBackgroundColor: Colors.transparent,
        fillChild: ShowCaseWidget(builder: Builder(builder: (_) => NewSqaure())),
        fillColor:  BoxDecoration(
          // color: fillColor,
          gradient: new LinearGradient(
            colors: [
              // const Color.fromRGBO(240, 241, 226, 100),
              // const Color.fromRGBO(240, 241, 226, 100)
              // const Color(0xFF0277BD),
              // Color.fromRGBO(22, 111, 123, 100)
              Colors.white,
              Colors.white
            ],
            begin: const FractionalOffset(0.0, 0.0),
            end:const FractionalOffset(1.0, 0.0),
          ),
            borderRadius: new BorderRadius.only(
              topLeft: const Radius.circular(40.0),
              topRight: const Radius.circular(40.0),
            )
        ),
      ), // HomeForeground
      //Color.fromRGBO(240, 241, 226, 100)
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