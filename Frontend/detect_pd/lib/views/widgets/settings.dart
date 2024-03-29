import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:shared_preferences/shared_preferences.dart';

class Settings extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        color: Color.fromRGBO(5, 88, 115, 100),
        //center the widgets in the body
        child: Center(
          child: Column(
            // creating the setting buttons
            children: <Widget>[
              SettingsButton(buttonName:"Guide me", width: 260.0,
                  height: 50.0,
                  bodyMargin: const EdgeInsets.only(left:30.0, top:30.0,right:30.0,bottom:5.0),
                  padding: EdgeInsets.all(5.0),
                  elevation: 6.0,
              ),  // SettingsButton
            ],  // <Widget>[]
          ),  // Column
        ),  // Center
      ),  // Container
    );  // Scaffold
  }
}

class SettingsButton extends StatelessWidget{

  // creating the variables
  final String buttonName;
  final width;
  final height;
  final bodyMargin;
  final padding;
  final elevation;

  // creating the constructor
  SettingsButton({this.buttonName, this.width, this.height, this.bodyMargin, this.padding, this.elevation});

  @override
  Widget build(BuildContext context) {

    return Container(
      width: width,
      height: height,
      margin: bodyMargin,
      // using the raised button widget with an icon
      child: RaisedButton.icon(
        shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(100),
            // side: BorderSide(color: Colors.grey, width: 1)
        ),  // RoundedRectangleBorder
        color: Colors.grey,
        icon: Icon(Icons.settings, color: Colors.white70,),
        label: Text(buttonName,
          style: TextStyle(
              color: Colors.white70
          ),  // TextStyle
        ),  // Text
        padding: padding,
        elevation: elevation,
        // function after pressing the button
        onPressed: () async {
          // clear shared preferences
          final sharedPreferences = await SharedPreferences.getInstance();
          await sharedPreferences.clear();
          print("Shared preferences cleared");

          Fluttertoast.showToast(
              msg: "Guide turned on for Home screen",
              backgroundColor: Colors.teal,
              textColor: Colors.white,
              fontSize: 16.0);
        },
      ),  // RaisedButton.icon
    );  // Container
  }
}



