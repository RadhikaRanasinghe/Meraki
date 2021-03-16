import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';



class ResultsForeground extends StatelessWidget {
  final mainBackgroundColor;
  final fillColor;
  final resultImage;
  final expandedHeight;
  final result;

  ResultsForeground({this.mainBackgroundColor, this.fillColor , this.resultImage,this.expandedHeight,this.result});

  @override
  Widget build(BuildContext context) {
    return CustomScrollView(
      slivers: <Widget>[
        SliverAppBar(
            floating: false,
            pinned: false,
            automaticallyImplyLeading: false,
            expandedHeight: expandedHeight,
            flexibleSpace: FlexibleSpaceBar(
                background:resultImage
            )
        ),
        SliverFillRemaining(
          child: Container(
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              color: mainBackgroundColor,
              child: Container(
                width: MediaQuery.of(context).size.width,
                height: MediaQuery.of(context).size.height,
                decoration: BoxDecoration(
                  color: fillColor,
                  borderRadius: BorderRadius.only(
                      topLeft: Radius.circular(40),
                      topRight: Radius.circular(40)),
                ),
                child:ResultsText(result: result,disclaimer: 'Disclaimer: Consult a medical professional for further clarification ',fontcolor:const Color(0xffe8e8e8)) ,
              )),
        ),
      ],
    );
  }
}

class ResultsText extends StatelessWidget{

  final result;
  final disclaimer;
  final fontcolor;



  ResultsText({this.result, this.disclaimer,this.fontcolor});
  @override
  Widget build(BuildContext context) {

    return Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: <Widget>[
          SizedBox(
            width: 450.0,
            height: 45.0,
            child: Text(
              'Results',
              style: TextStyle(
                fontFamily: 'Montserrat',
                fontSize: 31,
                color:fontcolor,
                fontWeight: FontWeight.w700,
                height: 0.6967741443264869,
              ),
              textAlign: TextAlign.center,
            ),
          ),
          SizedBox(
            width: 450.0,
            height: 131.0,
            child: Text(
              result,
              style: TextStyle(
                fontFamily: 'Montserrat',
                fontSize: 28,
                color: fontcolor,
                fontWeight: FontWeight.w700,
                height: 1.4285714285714286,
              ),
              textAlign: TextAlign.center,
            ),
          ),
          SizedBox(
            width: 450.0,
            child: Text(
              disclaimer,
              style: TextStyle(
                fontFamily: 'Montserrat',
                fontSize: 10,
                color: fontcolor,
                fontWeight: FontWeight.w700,
                height: 2.1599998474121094,
              ),
              textAlign: TextAlign.center,
            ),
          )
        ]);
  }

}
