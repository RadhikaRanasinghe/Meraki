import 'package:detect_pd/views/widgets/results-background.dart';
import 'package:detect_pd/views/widgets/results-foreground.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(

    initialRoute:'load' ,
    routes:{
      'load':(context) =>PositiveResultsPage(),
    },
    debugShowCheckedModeBanner: false,
  )); // MaterialApp
}


class PositiveResultsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.transparent,
      // building the positive result page body
      body: ResultsForeground(
          mainBackgroundColor: Colors.grey[400],
          fillColor: Color(0xFF01227D),
          foregroundColor: Color(0xFF01227D),
          borderColor: Color(0xFF01227D),
          resultImage: ResultBackground(
            resultBackgroundHeight: 500.0,
            resultBackgroundImage: 'assets/negativeBackground.png',
            resultsBackgroundCornerRadius: const Radius.circular(40.0),
          ), //ResultBackground
          expandedHeight: 300.0,
          result: 'Parkinson\'s Disease \n Detected!'), //ResultsForeground
    ); //Scaffold
  }
}
