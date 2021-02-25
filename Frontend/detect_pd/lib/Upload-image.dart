import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'package:http_parser/http_parser.dart';

class GalleryAccess extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => GalleryAccessState();
}

class GalleryAccessState extends State<GalleryAccess> {
  File galleryFile;
  File image;
  final picker = ImagePicker();

  Future<dynamic> pickImageFromGallery(ImageSource source) async {
    final image = await picker.getImage(source: source);

    setState(() {
      this.image = File(image.path);
    });
  }

  doUpload() {
    //TODO : Assign our API host address to this variable
    var request = http.MultipartRequest('POST', Uri.parse("url_to_api"));
    Map<String, String> headers = {"Content-type": "multipart/form-data"};
    request.files.add(
      http.MultipartFile(
        'image',
        image.readAsBytes().asStream(),
        image.lengthSync(),
        filename: "filename",
        contentType: MediaType('image', 'jpeg'),
      ),
    );
    request.headers.addAll(headers);
    print("request: " + request.toString());
    request.send().then((value) => print(value.statusCode));
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          child: new RaisedButton(
            child: new Text('Select Image from Gallery'),
            onPressed: () => pickImageFromGallery(ImageSource.gallery),
          ),
        ),
        SizedBox(
          height: 200.0,
          width: 300.0,
          child: image == null
              ? Center(child: new Text('Sorry nothing selected!!'))
              : Center(child: new Image.file(image)),
        )
      ],
    );
  }
}
