# Results

## 1. create some artists

```python
>>> from artists.models import Artist
>>> new_artist = Artist()
>>> new_artist.name = 'samy'
>>> new_artist.profile_link = 'https://www.instagram.com/samy/'
>>> new_artist.save()
>>> new_artist
<Artist: samy>
>>> new_artist = Artist()
>>> new_artist.name = 'saeed'
>>> new_artist.profile_link = 'https://www.instagram.com/saeed/'
>>> new_artist.save()
>>> new_artist
<Artist: saeed>
```

## 2. list down all artists

```python
 >>> from artists.models import Artist
 >>> Artist.objects.all()
 <QuerySet [<Artist: Mohamed khaled>, <Artist: ahmed>, <Artist: saeed>, <Artist: samy>]>
```

## 3. list down all artists sorted by name

```python
  >>> from artists.models import Artist
  >>> Artist.objects.order_by('name')
  <QuerySet [<Artist: Mohamed khaled>, <Artist: ahmed>, <Artist: saeed>, <Artist: samy>]>
```
## 4. list down all artists whose name starts with `a`
```python
  >>> from artists.models import Artist
  >>> Artist.objects.filter(name__startswith='a')
  <QuerySet [<Artist: ahmed>]>
```
## 5. in 2 different ways, create some albums and assign them to any artists (hint: use `objects` manager and use the related object reference)
```python
>>> from albums.models import Album
>>> album=Album(name='album1',cost='5.6')
>>> album.save()
>>> album=Album(name='album2',cost='9.6')
>>> album.save()
>>>artist=Artist.objects.get(name='ahmed')
>>>album=Album.objects.get(name='album1')
>>> artist_albums=ArtistAlbum(artist=artist,album=album)
>>> artist_albums.save()                                
>>> album=Album.objects.get(name='album2') 
>>> artist_albums=ArtistAlbum(artist=artist,album=album) 
>>> artist_albums.save()
>>> Album.objects.all()                   
<QuerySet [<Album: album1>, <Album: album2>]>
```
## 6. get the latest released album
```python
>>> from albums.models import Album
>>> Album.objects.latest('release_date')
<Album: album2>
```
## 7. get all albums released before today
```python
>>> from albums.models import Album
>>> from datetime import datetime
>>> Album.objects.filter(release_datetime__lt=datetime.today())
<QuerySet [<Album: album1>, <Album: album2>]>
```
## 8. get all albums released today or before but not after today
```python
>>> from albums.models import Album
>>> from datetime import datetime
>>> Album.objects.filter(release_datetime__lte=datetime.today())
<QuerySet [<Album: album1>, <Album: album2>]>
```
## 9. count the total number of albums
```python
>>> from albums.models import Album
>>> Album.objects.count()
2
```
## 10. in 2 different ways, for each artist, list down all of his/her albums (hint: use objects manager and use the related object reference)
```python
>>> from artists.models import Artist
>>> from albums.models import Album
>>> from artists.models import ArtistAlbum
>>> artist=Artist.objects.get(name='ahmed')
>>> ArtistAlbum.objects.filter(artist=artist)
<QuerySet [<ArtistAlbum: ahmed - album1>]>
>>> artist=Artist.objects.get(name='Mohamed Khaled')
>>> ArtistAlbum.objects.filter(artist=artist)
<QuerySet [<ArtistAlbum: Mohamed Khaled - album2>]>
```
## 11 . list down all albums ordered by cost then by name (cost has the higher priority)
```python
>>> from albums.models import Album
>>> Album.objects.order_by('cost','name')
<QuerySet [<Album: album1>, <Album: album2>]>
```
