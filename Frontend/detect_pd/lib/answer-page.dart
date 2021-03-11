import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'widgets/home-background.dart';
import 'widgets/home-foreground.dart';


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
            title: 'FAQ',
            logoPath: 'assets/testImage.jpg',
            height: 10.0,
            bigSquareColor: Color.fromRGBO(22, 111, 123, 100),
            smallSquareColor: Color.fromRGBO(169, 229, 238, 30),
            backgroundColor: Color.fromRGBO(94, 163, 184, 100),
          ),
          appBarBackgroundColor: Color.fromRGBO(94, 163, 184, 100),
          fillChild: answerForeground(question:'question 1', answer:'test'),
          fillColor: Color.fromRGBO(240, 241, 226, 100),
        ));
  }
}

class answerForeground extends StatelessWidget {
  final question;
  final answer;

  answerForeground({this.question, this.answer});

  @override
  Widget build(BuildContext context) {
    return Container(
      child: new Center(
        child: Column(
          children: [
            SizedBox(height: 30),
            Container(
              child: Center(
                  child: Text(
                    question,
                    style: TextStyle(color: Colors.white),
                  )),
              width: 270.0,
              height: 46.0,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(33.0),
                color: const Color(0xff687b8d),
                boxShadow: [
                  BoxShadow(
                    color: const Color(0x29000000),
                    offset: Offset(0, 3),
                    blurRadius: 10,
                  ),
                ],
              ),
            ),
            SizedBox(height: 30),
            Container(
              child: Padding(
                padding: const EdgeInsets.fromLTRB(20, 50, 20, 20),
                child: Text(
                  answer,
                  style: TextStyle(color: Colors.white),
                ),
              ),
              width: 270.0,
              height: 369.0,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(33.0),
                color: const Color(0xff687b8d),
                boxShadow: [
                  BoxShadow(
                    color: const Color(0x29000000),
                    offset: Offset(0, 3),
                    blurRadius: 10,
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
      width: 314.0,
      height: 541.0,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20.0),
        color: const Color(0xfff0f1e2),
        boxShadow: [
          BoxShadow(
            color: const Color(0x29000000),
            offset: Offset(0, 3),
            blurRadius: 10,
          ),
        ],
      ),
    );
  }
}