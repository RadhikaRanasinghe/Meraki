import 'package:detect_pd/services/api-camera.dart';
import 'package:detect_pd/views/ui/settings-page.dart';
import 'package:detect_pd/views/widgets/navbar.dart';
import 'package:flutter/material.dart';
import 'package:detect_pd/views/widgets/home-foreground.dart';
import 'package:detect_pd/views/ui/main.dart';

class CameraFormPage extends StatefulWidget {
  @override
  _CameraFormPageState createState() => _CameraFormPageState();
}

class _CameraFormPageState extends State<CameraFormPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HomeForeground(
        expandedHeight: null,
        appBarChild: Text('home Background'),
        appBarBackgroundColor:Color.fromRGBO(118, 176, 195, 100),
        fillChild: CameraAccess(),
        // fillColor:  Color.fromRGBO(240, 241, 226, 100),
        fillColor:  Color(0xfff9fbe7),
      ),
      bottomNavigationBar: NavBar(
        link1: null,
        link2: (){
          Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (context) => HomePage()));
        },
        link3: (){
          Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (context) => SettingsPage()));
        },
      ),
    );
  }
}