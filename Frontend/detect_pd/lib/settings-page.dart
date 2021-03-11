import 'package:detect_pd/widgets/home-buttons.dart';
import 'package:detect_pd/widgets/Settings.dart';
import 'package:detect_pd/widgets/home-background.dart';
import 'package:detect_pd/widgets/navbar.dart';
import 'package:flutter/material.dart';
import 'FAQ-Page.dart';
import 'widgets/home-Foreground.dart';
import 'main.dart';

// void main() {
//   runApp(MaterialApp(
//     home: SettingsPage(),
//     debugShowCheckedModeBanner: false,
//   ));
// }

class SettingsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HomeForeground(
        expandedHeight: 153.0,
        appBarChild: HomeBackground(
          title: 'Settings',
          logoPath: 'assets/pd_log_bg_small.png',
          height: 153.0,
          bigSquareColor: Color.fromRGBO(22, 111, 123, 100),
          smallSquareColor: Color.fromRGBO(169, 229, 238, 30),
          backgroundColor: Color.fromRGBO(94, 163, 184, 100),
          titleColor: Colors.white,
        ),
        appBarBackgroundColor: Color.fromRGBO(94, 163, 184, 100),
        fillChild: Settings(),
        fillColor:  Color.fromRGBO(240, 241, 226, 100),
      ),
      bottomNavigationBar: NavBar(
        link1: null,
        link2: (){
          Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => HomePage()));
        },
        link3: null,
        backgroundColor: Color.fromRGBO(240, 241, 226, 100) ,
      ),
    );
  }
}