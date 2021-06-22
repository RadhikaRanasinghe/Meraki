import 'package:flutter/material.dart';

class ResultBackground extends StatelessWidget {
  final resultBackgroundHeight;
  final resultBackgroundImage;
  final resultsBackgroundCornerRadius;

  const ResultBackground({this.resultBackgroundHeight, this.resultBackgroundImage, this.resultsBackgroundCornerRadius});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width,
      height: resultBackgroundHeight,
      decoration: BoxDecoration(
          color: Colors.transparent,
          image: DecorationImage(
              image: AssetImage(resultBackgroundImage),
              fit: BoxFit.cover
          ), // DecorationImage
          borderRadius: new BorderRadius.only(
            bottomLeft: resultsBackgroundCornerRadius,
            bottomRight: resultsBackgroundCornerRadius,
          ),
      ), // BoxDecoration
    ); // Container
  }
}