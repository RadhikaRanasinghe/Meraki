import 'package:flutter/material.dart';

class ResultBackground extends StatelessWidget {
  final resultBackgroundHeight;
  final resultBackgroundImage;

  const ResultBackground({this.resultBackgroundHeight, this.resultBackgroundImage});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width,
      height: resultBackgroundHeight,
      decoration: BoxDecoration(
          image: DecorationImage(
              image: AssetImage(resultBackgroundImage),
              fit: BoxFit.cover
          ) // DecorationImage
      ), // BoxDecoration
    ); // Container
  }
}