import 'package:detect_pd/views/widgets/results-background.dart';
import 'package:detect_pd/views/widgets/results-foreground.dart';
import 'package:flutter/material.dart';

class PositiveResultsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // building the positive result page body
      body: ResultsForeground(
          mainBackgroundColor: Colors.grey[400],
          fillColor: Color(0xFF01227D),
          resultImage: ResultBackground(
            resultBackgroundHeight: 460.0,
            resultBackgroundImage: 'assets/negativeBackground.png',
          ),
          //ResultBackground
          expandedHeight: 300.0,
          result: 'Parkinson\'s Disease \n Detected!'), //ResultsForeground
    ); //Scaffold
  }
}
