import 'package:detect_pd/views/ui/settings-page.dart';
import 'package:detect_pd/views/widgets/home-background.dart';
import 'package:detect_pd/views/widgets/home-foreground.dart';
import 'package:detect_pd/views/widgets/navbar.dart';
import 'package:detect_pd/views/ui/answer-page.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:detect_pd/views/ui/main.dart';

class FaqPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // building the main interface of the page
    return Scaffold(
      body: HomeForeground(
        expandedHeight: 153.0,
        appBarChild: HomeBackground(
          title: 'FAQ',
          logoPath: 'assets/pd_log_bg_small.png',
          height: 153.0,
          bigSquareColor: Color.fromRGBO(22, 111, 123, 100),
          smallSquareColor: Color.fromRGBO(169, 229, 238, 30),
          backgroundColor: Color.fromRGBO(94, 163, 184, 100),
          titleColor: Colors.white,
        ),
        //HomeBackground
        appBarBackgroundColor: Color.fromRGBO(94, 163, 184, 100),

        fillChild: FaqForground(spacing: 40.0),
        fillColor: Color.fromRGBO(240, 241, 226, 100),
      ), //HomeBackground
      bottomNavigationBar: NavBar(
        link1: null,
        link2: () {
          Navigator.pushReplacement(
              context, MaterialPageRoute(builder: (context) => HomePage()));
        },
        link3: () {
          Navigator.pushReplacement(
              context, MaterialPageRoute(builder: (context) => SettingsPage()));
        },
        backgroundColor: Color.fromRGBO(240, 241, 226, 100),
      ), //NavBar
    ); //Scaffold
  }
}

class FaqForground extends StatelessWidget {
  final spacing;


  FaqForground({this.spacing});

  @override
  Widget build(BuildContext context) {
    return Container(
        child: new Center(
            child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
          GreyButtons(buttonText: 'What color pen should be used for the test?',function:() {
            Navigator.pushNamed(
                context,'/answers-page',arguments:1 );
          }),
          SizedBox(height: spacing),
          GreyButtons(buttonText: 'If the test result is positive can the patient know which stage they are at?',function:() {
            Navigator.pushNamed(
                context,'/answers-page',arguments:2 );
          }),
          SizedBox(height: spacing),
          GreyButtons(buttonText: 'What should I do if I get a positive result?',function:() {
            Navigator.pushNamed(
                context,'/answers-page',arguments:3 );
          }),
          SizedBox(height: spacing),
          GreyButtons(buttonText: 'How accurate is the test result?',function:() {
            Navigator.pushNamed(
                context,'/answers-page',arguments:4 );
          })
        ] //<widget>[]
                ) //Column
            ) //Center
        ); //Container
  }
}

class GreyButtons extends StatelessWidget {
  final buttonText;
  final function;

  GreyButtons({this.buttonText, this.function});

  // template for FAQ button
  @override
  Widget build(BuildContext context) {
    return Container(
      child: new Center(
        child: InkWell(
            onTap: function,
            child: Container(
              child: Padding(
                padding: const EdgeInsets.all(10.0),
                child: new Text(buttonText, textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Colors.white,
                    ) //TextStyle
                    ),
              ), //Text
            ) //Container
            ), //Inkwell
      ), //Center
      width: 390.0,
      height: 60.0,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(33.0),
        color: const Color(0xff687b8d),
        boxShadow: [
          BoxShadow(
            color: const Color(0x29000000),
            offset: Offset(0, 3),
            blurRadius: 6,
          ), //BoxShadow
        ],
      ), //BoxDecoration
    ); //Container
  }
}
