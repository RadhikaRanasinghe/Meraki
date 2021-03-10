import 'dart:math';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'home-Foreground.dart';
import 'home-background.dart';

void main() => runApp(MaterialApp(
  home: Home(),
));

class Home extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: HomeForeground(
          expandedHeight: 153.0,
          appBarChild: HomeBackground(
            title: '',
            logoPath: 'assets/testImage.jpg',
            height: 10.0,
            bigSquareColor: Color.fromRGBO(22, 111, 123, 100),
            smallSquareColor: Color.fromRGBO(169, 229, 238, 30),
            backgroundColor: Color.fromRGBO(94, 163, 184, 100),
          ),
          appBarBackgroundColor: Color.fromRGBO(94, 163, 184, 100),
          fillChild:Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Center(
                child: Loader(),
              ),
              SizedBox(height: 50),
              Text("Processing!",style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20,color:Colors.white),)
            ],
          ),
          fillColor:  Color.fromRGBO(240, 241, 226, 100),
        )
    );
  }
}


class Loader extends StatefulWidget {
  @override
  LoaderState createState() => LoaderState();
}

class LoaderState extends State<Loader> with SingleTickerProviderStateMixin {
  AnimationController controller;
  Animation<double> animationRotation;
  Animation<double> animationRadiusIn;
  Animation<double> animationRadiusOut;

  final double initialRadius = 50;
  double radius = 0.0;

  @override
  void initState() {
    super.initState();
    controller =
        AnimationController(vsync: this, duration: Duration(seconds: 5));

    animationRotation = Tween<double>(
      begin: 0.0,
      end: 1.0,
    ).animate(CurvedAnimation(
        parent: controller, curve: Interval(0.0, 1.0, curve: Curves.linear)));
    animationRadiusIn = Tween<double>(
      begin: 1.0,
      end: 0.0,
    ).animate(CurvedAnimation(
        parent: controller,
        curve: Interval(0.75, 1.0, curve: Curves.elasticIn)));

    animationRadiusOut = Tween<double>(
      begin: 0.0,
      end: 1.0,
    ).animate(CurvedAnimation(
        parent: controller,
        curve: Interval(0.0, 0.25, curve: Curves.elasticOut)));

    controller.addListener(() {
      setState(() {
        if (controller.value >= 0.75 && controller.value <= 1.0) {
          radius = animationRadiusIn.value * initialRadius;
        } else if (controller.value >= 0.0 && controller.value <= 0.25) {
          radius = animationRadiusOut.value * initialRadius;
        }
      });
    });
    controller.repeat();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
        width: 100.0,
        height: 100.0,
        child: Center(
            child: RotationTransition(
              turns: animationRotation,
              child: Stack(children: <Widget>[
                Dot(
                  radius: 30.0,
                  color: Colors.black12,
                ),
                Transform.translate(
                  offset: Offset(radius * cos(pi / 4), radius * sin(pi / 4)),
                  child: Dot(radius: 10.0, color: Colors.teal.shade700),
                ),
                Transform.translate(
                  offset:
                  Offset(radius * cos(2 * pi / 4), radius * sin(2 * pi / 4)),
                  child: Dot(radius: 10.0, color: Colors.blue.shade900),
                ),
                Transform.translate(
                  offset:
                  Offset(radius * cos(3 * pi / 4), radius * sin(3 * pi / 4)),
                  child: Dot(radius: 10.0, color: Colors.teal.shade300),
                ),
                Transform.translate(
                  offset:
                  Offset(radius * cos(4 * pi / 4), radius * sin(4 * pi / 4)),
                  child: Dot(radius: 10.0, color: Colors.yellow.shade100),
                ),
                Transform.translate(
                  offset:
                  Offset(radius * cos(5 * pi / 4), radius * sin(5 * pi / 4)),
                  child: Dot(radius: 10.0, color: Colors.teal.shade700),
                ),
                Transform.translate(
                  offset:
                  Offset(radius * cos(6 * pi / 4), radius * sin(6 * pi / 4)),
                  child: Dot(radius: 10.0, color: Colors.blue.shade900),
                ),
                Transform.translate(
                  offset:
                  Offset(radius * cos(7 * pi / 4), radius * sin(7 * pi / 4)),
                  child: Dot(radius: 10.0, color: Colors.teal.shade300),
                ),
                Transform.translate(
                  offset:
                  Offset(radius * cos(8 * pi / 4), radius * sin(8 * pi / 4)),
                  child: Dot(radius: 10.0, color: Colors.yellow.shade100),
                ),
              ]),
            )));
  }
}

class Dot extends StatelessWidget {
  final double radius;
  final Color color;

  Dot({this.radius, this.color});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        width: this.radius,
        height: this.radius,
        decoration: BoxDecoration(color: this.color, shape: BoxShape.circle),
      ),
    );
  }
}