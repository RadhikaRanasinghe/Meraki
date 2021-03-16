import 'package:detect_pd/services/api-gallery.dart';
import 'package:detect_pd/settings-page.dart';
import 'package:detect_pd/widgets/navbar.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'widgets/home-foreground.dart';
import 'main.dart';

void main() {
  runApp(MaterialApp(
      home: GalleryFormPage(),
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        canvasColor: Color.fromRGBO(118, 176, 195, 100),
      )
  ));
}

// -------------------------------------------------------------------------- //
class GalleryFormPage extends StatefulWidget {
  @override
  _GalleryFormPageState createState() => _GalleryFormPageState();
}

class _GalleryFormPageState extends State<GalleryFormPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: HomeForeground(
        expandedHeight: null,
        appBarChild: Text('home Background'),
        appBarBackgroundColor:Color.fromRGBO(118, 176, 195, 100),
        fillChild: GalleryAccess(),
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