import 'package:detect_pd/utils/url-launcher.dart';
import 'package:detect_pd/views/widgets/home-buttons.dart';
import 'package:detect_pd/views/widgets/Settings.dart';
import 'package:detect_pd/views/widgets/home-background.dart';
import 'package:detect_pd/views/widgets/navbar.dart';
import 'package:flutter/material.dart';
import 'package:detect_pd/views/ui/about-page.dart';
import 'package:detect_pd/views/widgets/home-Foreground.dart';
import 'package:detect_pd/main.dart';

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
          backgroundColor: Colors.transparent,
          titleColor: Colors.white,
        ),
        appBarBackgroundColor: Colors.transparent,
        fillChild: Settings(),
        fillColor:   BoxDecoration(
          // color: fillColor,
            gradient: new LinearGradient(
              colors: [
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
      ),
      bottomNavigationBar: NavBar(
        link1: launcher,
        link2: (){
          Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (context) => HomePage()));
        },
        link3: null,
        backgroundColor: Colors.transparent,
      ),
    );
  }
}