import 'package:detect_pd/results-background.dart';
import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(
  home: ResultBackgroundWidgetPos(),
));

class ResultBackgroundWidgetPos extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ResultBackground(
        resultBackgroundHeight: 460.0,
        resultBackgroundImage: 'assets/negativeBackground.png',
      ),
    );
  }
}