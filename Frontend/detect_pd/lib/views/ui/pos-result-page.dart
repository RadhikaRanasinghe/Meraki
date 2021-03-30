import 'package:detect_pd/views/ui/settings-page.dart';
import 'package:detect_pd/views/widgets/navbar.dart';
import 'package:detect_pd/views/widgets/results-background.dart';
import 'package:detect_pd/views/widgets/results-foreground.dart';
import 'package:flutter/material.dart';

import 'package:detect_pd/views/ui/about-page.dart';
import 'package:detect_pd/views/ui/main.dart';


void main() =>
    runApp(MaterialApp(
      home: PositiveResultsPage(),
    ));

class PositiveResultsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ResultsForeground(mainBackgroundColor: Colors.grey[400],
          fillColor: Colors.cyan.shade800,
          resultImage: ResultBackground(
              resultBackgroundHeight: 460.0,
              resultBackgroundImage: 'assets/negativeBackground.png',
          ),
          expandedHeight: 300.0,
          result: 'Parkinson\'s Disease \n Detected!'),
      // bottomNavigationBar: NavBar(
      //   link1: () {
      //     Navigator.pushReplacement(
      //         context,
      //         MaterialPageRoute(builder: (context) => AboutPDPage()));
      //   },
      //   link2: () {
      //     Navigator.pushReplacement(
      //         context,
      //         MaterialPageRoute(builder: (context) => HomePage()));
      //   },
      //   link3: () {
      //     Navigator.pushReplacement(
      //         context,
      //         MaterialPageRoute(builder: (context) => SettingsPage()));
      //   },
      //   backgroundColor: Color.fromRGBO(240, 241, 226, 100),
      // ),
    );
  }
}