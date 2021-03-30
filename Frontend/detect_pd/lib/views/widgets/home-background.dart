import 'package:flutter/material.dart';

class HomeBackground extends StatelessWidget {
  final title;
  final height;
  final bigSquareColor;
  final smallSquareColor;
  final backgroundColor;
  final logoPath;
  final titleColor;

  HomeBackground({this.title, this.height, this.bigSquareColor, this.backgroundColor, this.smallSquareColor, this.logoPath, this.titleColor});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width,
      height: height,
      color: backgroundColor,
      child: Stack(
        children: [
          Positioned(
            top: -47,
            left: -41,
            child: Square(
              color:  bigSquareColor,
              size: 142.0,
              borderRadius: 31.0,
            ),
          ),
          Positioned(
            top: -37,
            left: 58,
            child: Square(
              color: smallSquareColor,
              size: 93.0,
              borderRadius: 18.0,
            ),
          ),
          Positioned(
            top: 102,
            left : 40,
            child: FlatButton(
              onPressed: () {},
              child: Text(title,
                style: TextStyle(
                  fontSize: 25,
                  fontWeight: FontWeight.bold,
                  color: titleColor
                ),
              ),
            ),
          ),
          Positioned(
            top: 65,
            left: 241,
            child: Image(
              image: AssetImage(logoPath),
              width: 134,
              height: 88,
            ),
          ),
        ],
      ),
    );
  }
}

class Square extends StatelessWidget {
  final color;
  final size;
  final borderRadius;

  Square({this.color, this.size, this.borderRadius});

  @override
  Widget build(BuildContext context) {
    return Container (
      width: size,
      height: size,
      decoration: BoxDecoration(
          color: color,
          borderRadius: BorderRadius.all(Radius.circular(borderRadius))
      ),
    );
  }
}