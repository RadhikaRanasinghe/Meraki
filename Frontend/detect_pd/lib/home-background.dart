import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(
  home: Home(),
));

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body:HomeBackground(
        title: 'Home',
        height: 153.0,
      ),
    );
  }
}

class HomeBackground extends StatelessWidget {
  final title;
  final height;

  HomeBackground({this.title, this.height});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width,
      height: height,
      color: Color.fromRGBO(94, 163, 184, 100),
      child: Stack(
        children: [
          Positioned(
            top: -47,
            left: -41,
            child: Square(
              color:  Color.fromRGBO(22, 111, 123, 100),
              size: 142.0,
              borderRadius: 31.0,
            ),
          ),
          Positioned(
            top: -37,
            left: 58,
            child: Square(
              color: Color.fromRGBO(169, 229, 238, 30),
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
                    fontSize: 20
                ),
              ),
            ),
          ),
          Positioned(
            top: 65,
            left: 241,
            child: Image(
              image: AssetImage('assets/testImage.jpg'),
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