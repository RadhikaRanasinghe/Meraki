// ignore: avoid_web_libraries_in_flutter

import 'dart:io';

import 'package:dio/dio.dart';
import 'package:ext_storage/ext_storage.dart';

import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:permission_handler/permission_handler.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyPdf(),
    );
  }
}

class MyPdf extends StatefulWidget {
  @override
  _MyPdfState createState() => _MyPdfState();
}

class _MyPdfState extends State<MyPdf> {
  final imgUrl =
      "http://pdfhost.io/edit?doc=f47bb0d6-d7fe-41c8-bfaf-187b8af974d5";
      // "http://www.pdf995.com/samples/pdf.pdf";

  // "http://filebin.net/36ij8cgovxl519na/Meander_template.pdf?t=tb9oa1y3";

  var dio = Dio();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Center(
            child: RaisedButton.icon(
                onPressed: () async {
                  String path =
                      await ExtStorage.getExternalStoragePublicDirectory(
                          ExtStorage.DIRECTORY_DOWNLOADS);
                  String fullPath = "$path/MeanderTemplate.pdf";
                  download2(dio, imgUrl, fullPath);
                },
                icon: Icon(Icons.file_download),
                label: Text('Download')),
          ),
        ],
      ),
    );
  }

  @override
  void initState() {
    getPermission();
  }

  void getPermission() async {
    print("getPermission");
    await PermissionHandler().requestPermissions([PermissionGroup.storage]);
  }

  Future download2(Dio dio, String url, String savePath) async {
    //get pdf from link
    try {
      Response response = await dio.get(
        url,
        onReceiveProgress: showDownloadProgress,
        //Received data with List<int>
        options: Options(
            responseType: ResponseType.bytes,
            followRedirects: false,
            validateStatus: (status) {
              return status < 500;
            }),
      );

      //write in download folder
      File file = File(savePath);
      var raf = file.openSync(mode: FileMode.write);
      raf.writeFromSync(response.data);
      await raf.close();
    } catch (e) {
      print("error is");
      print(e);
    }
  }

  void showDownloadProgress(received, total) {
    double value = received / total * 100;
    if (total != -1) {
      print((received / total * 100).toStringAsFixed(0) + "%");
    }
    if (value == 100.0) {
      Fluttertoast.showToast(
        msg: "Download Complete !",
          backgroundColor: Colors.teal,
          textColor: Colors.white,
          fontSize: 16.0);
    }
  }
}
