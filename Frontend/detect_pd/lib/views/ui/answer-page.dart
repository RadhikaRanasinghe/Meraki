import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:detect_pd/views/widgets/home-background.dart';
import 'package:detect_pd/views/widgets/home-foreground.dart';

class AnswerPage extends StatelessWidget {
  int quesNum;
  String question;
  String answer;
  @override
  Widget build(BuildContext context) {

    quesNum =ModalRoute.of(context).settings.arguments;
    if(quesNum == 1){
      question='What color pen should be used for the test?';
      answer='•	The recommendation is to do the test with a blue color pen';
    }else if (quesNum == 2){
      question='If the test result is positive can patient know which stage Parkinsons is at?';
      answer='•	No. You can only know whether it is positive or negative.';
    }else if (quesNum == 3){
      question='What should I do if I get a positive result?';
      answer='•	If so, you should consult a Healthcare Professional and start the treatments.';
    }else if (quesNum == 4){
      question='How accurate is the test result?';
      answer='The results are relatively accurate , but it is always advised to meet with a medical professional ';
    }


    return Scaffold(
        body: HomeForeground(
          expandedHeight: 153.0,
          appBarChild: HomeBackground(
            title: 'FAQ',
            logoPath: 'assets/pd_log_bg_small.png',
            height: 10.0,
            bigSquareColor: Color.fromRGBO(22, 111, 123, 100),
            smallSquareColor: Color.fromRGBO(169, 229, 238, 30),
            backgroundColor: Color.fromRGBO(94, 163, 184, 100),
            titleColor: Colors.white,
          ),//HomeBackground
          appBarBackgroundColor: Color.fromRGBO(94, 163, 184, 100),
          fillChild: answerForeground(question:question, answer:answer),
          fillColor: Color.fromRGBO(240, 241, 226, 100),
        ));//HomeBackground,Scaffold
  }
}

class answerForeground extends StatelessWidget {
  final question;
  final answer;

  answerForeground({this.question, this.answer});
// building the page foreground
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
                    question, textAlign: TextAlign.center,
                    style: TextStyle(color: Colors.white),
                  )),//Text,Center
              width: 310.0,
              height: 46.0,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(33.0),
                color: const Color(0xff687b8d),
                boxShadow: [
                  BoxShadow(
                    color: const Color(0x29000000),
                    offset: Offset(0, 3),
                    blurRadius: 10,
                  ),//BoxShadow
                ],
              ),//BoxDecoration
            ),//Container
            SizedBox(height: 30),
            Container(
              child: Padding(
                padding: const EdgeInsets.fromLTRB(20, 50, 20, 20),
                child: Text(
                  answer,
                  style: TextStyle(color: Colors.white),
                ), // Text
              ),// Padding
              width: 290.0,
              height: 369.0,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(33.0),
                color: const Color(0xff687b8d),
                boxShadow: [
                  BoxShadow(
                    color: const Color(0x29000000),
                    offset: Offset(0, 3),
                    blurRadius: 10,
                  ),//BoxShadow
                ],
              ),//BoxDecoration
            ),//Container
          ],
        ),//Column
      ),//Center
      width: 340.0,
      height: 541.0,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20.0),
        color: const Color(0xfff0f1e2),
        boxShadow: [
          BoxShadow(
            color: const Color(0x29000000),
            offset: Offset(0, 3),
            blurRadius: 10,
          ),//BoxShadow
        ],
      ),//BoxDecoration
    );//Container
  }
}