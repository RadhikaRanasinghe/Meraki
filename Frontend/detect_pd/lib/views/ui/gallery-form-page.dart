import 'package:detect_pd/services/api-gallery.dart';
import 'package:detect_pd/utils/url-launcher.dart';
import 'package:detect_pd/views/ui/settings-page.dart';
import 'package:detect_pd/views/widgets/navbar.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:detect_pd/views/widgets/home-foreground.dart';
import 'package:detect_pd/main.dart';

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
        appBarBackgroundColor:Colors.transparent,
        fillChild: GalleryAccess(),
        fillColor:  BoxDecoration(
          // color: fillColor,
            gradient: new LinearGradient(
              colors: [
                Colors.white,
                Colors.white
              ],
              begin: const FractionalOffset(0.0, 0.0),
              end:const FractionalOffset(1.0, 0.0),
            ),
            borderRadius: new BorderRadius.only(
              topLeft: const Radius.circular(40.0),
              topRight: const Radius.circular(40.0),
            )
        ),
      ), // HomeForeground
      bottomNavigationBar: NavBar(
        link1: launcher,
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