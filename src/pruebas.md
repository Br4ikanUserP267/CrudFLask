id = db.insert({
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']

    })
    return jsonify(str(Object(id)))


users =[]
    for user in db.find():
        users.append(

            {
                '_id': str(ObjectId(doc['id'])),
                'name': doc['name'],
                'email': doc['email'],
                'password': doc['password']
            })
    return jsonify(users)

