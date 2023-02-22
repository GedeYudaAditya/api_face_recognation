from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Test, Face, Image
from .serializers import TestSerializer, FaceSerializer, ImageSerializer

import cv2 as cv
import numpy as np
import uuid

# load trained model
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

@api_view(['GET'])
def getTest(request):
    data = Test.objects.all()
    serializer = TestSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTest(request):
    data = request.data
    serializer = TestSerializer(data=data, many=False)
    if serializer.is_valid(): 
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getFace(request):
    data = Face.objects.all()
    serializer = FaceSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addFace(request):
    data = request.data
    serializer = FaceSerializer(data=data, many=False)
    if serializer.is_valid(): 
        serializer.save()
    return Response(serializer.data)

# recognize faces function
@api_view(['POST'])
def recognizeFace(request):
    # Ambil data gambar dari request
    face_request = None
    image = request.FILES.get('image').read()

    try:
        # Konversi gambar ke format numpy array
        image = np.frombuffer(image, np.uint8)
        image = cv.imdecode(image, cv.IMREAD_COLOR)

        # Konversi gambar ke grayscale
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        # Deteksi wajah
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Mengambil data wajah
        for (x, y, w, h) in faces:
            # Crop gambar wajah
            face_request = gray[y:y+h, x:x+w]

        # ambil semua data wajah yang ada lalu bandingkan
        results = []
        faces2 = Face.objects.all()
        for face in faces2:
            face_image = face.face_image

            # ambil gambar wajah yang ada di static folder
            face_image = open('api/static/api/image/' + face_image, 'rb').read()

            face_image = np.frombuffer(face_image, np.uint8)
            face_image = cv.imdecode(face_image, cv.IMREAD_GRAYSCALE)

            # bandingkan data wajah yang ada dengan data wajah yang diupload
            result = cv.matchTemplate(face_request, face_image, cv.TM_CCOEFF_NORMED)

            results.append({'name': face.name, 'kemiripan': str(result[0][0])})

            # tentukan nilai kemiripan
            threshold = 0.7
            loc = np.where(result >= threshold)

            # jika nilai kemiripan lebih dari 70% maka wajah cocok
            if len(loc[0]) > 0:
                return Response({'status': 'Dikenali' ,'name': face.name, 'kemiripan': str(result[0][0])})
            
        return Response({'status': 'Tidak dikenali', 'record': results})
                

    except Exception as e:
        return Response({'error': str(e)})
        
    


# Endpoint untuk face detection
@api_view(['POST'])
def face_detection(request):
    face = None
    # Ambil data gambar dari request
    image = request.FILES.get('image').read()
    person_name = request.data.get('name')
    
    try:
        # Konversi gambar ke format numpy array
        image = np.frombuffer(image, np.uint8)
        image = cv.imdecode(image, cv.IMREAD_COLOR)

        # Konversi gambar ke grayscale
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        # hilangakn background
        # gray = cv.bilateralFilter(gray, 11, 17, 17)

        # Deteksi wajah
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Mengambil data wajah
        for (x, y, w, h) in faces:
            face = image[y:y+h, x:x+w]


        # Konversi data wajah ke format JSON
        # data = {'face': face.tolist()}
        # return Response(data
        
        # Simpan gambar ke static/images dengan nama random
        # berikan nama random untuk menghindari nama file yang sama

        # Generate nama file random
        filename = str(uuid.uuid4()) + '.jpg'

        # Simpan gambar ke static/images
        if face is not None:
            cv.imwrite('api/static/api/image/' + filename, face)

            # simpan ke database
            serializers = FaceSerializer(data={'name': person_name, 'face_image': filename, 'url': request.build_absolute_uri('static/api/image/' + filename)})
            if serializers.is_valid():
                serializers.save()

            return Response(serializers.data)

        return Response({'message': 'failed', 'error': 'cannot detect face'})
        
    except Exception as e:
        return Response({'message': 'failed', 'error': str(e)})

