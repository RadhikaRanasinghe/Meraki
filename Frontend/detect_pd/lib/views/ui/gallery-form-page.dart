import 'package:detect_pd/services/api-gallery.dart';
import 'package:detect_pd/views/ui/settings-page.dart';
import 'package:detect_pd/views/widgets/navbar.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:detect_pd/views/widgets/home-foreground.dart';
import 'package:detect_pd/views/ui/main.dart';

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
        fillColor:  Color(0xfff9fbe7),
      ), // HomeForeground
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
      ), // NavBar
    ); // Scaffold
  }
}