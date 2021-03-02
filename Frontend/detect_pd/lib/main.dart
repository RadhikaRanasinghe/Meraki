import 'package:detect_pd/HomeButtons.dart';
import 'package:detect_pd/Settings.dart';
import 'package:detect_pd/home-background.dart';
import 'package:detect_pd/navbar.dart';
import 'package:flutter/material.dart';
import 'FAQ-Page.dart';
import 'home-Foreground.dart';

void main() {
  runApp(MaterialApp(
      home: TestHome(),
    debugShowCheckedModeBanner: false,
  ));
}

class TestHome extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HomeForeground(
        expandedHeight: 153.0,
        appBarChild: HomeBackground(
          title: 'Home',
          logoPath: 'assets/testImage.jpg',
          height: 153.0,
          bigSquareColor: Color.fromRGBO(22, 111, 123, 100),
          smallSquareColor: Color.fromRGBO(169, 229, 238, 30),
          backgroundColor: Color.fromRGBO(94, 163, 184, 100),
          titleColor: Colors.white,
        ),
        appBarBackgroundColor: Color.fromRGBO(94, 163, 184, 100),
        // fillChild: Buttons(),
        // fillChild: Settings(),
        fillChild: FaqForground(spacing:40.0),
        fillColor:  Color.fromRGBO(240, 241, 226, 100),
      ),
      bottomNavigationBar: NavBar(
        link1: null,
        link2: null,
        link3: null,
        backgroundColor: Color.fromRGBO(240, 241, 226, 100) ,
      ),
    );
  }
}