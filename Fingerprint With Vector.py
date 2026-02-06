
python
import cv2
import numpy as np

# خواندن تصویر اثر انگشت
img = cv2.imread('fingerprint.png', 0)

# استفاده از الگوریتم ادوزن برای بهبود تصویر
img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

# استخراج نقاط مهم با استفاده از الگوریتم Harris
dst = cv2.cornerHarris(img,2,3,0.04)

# بردار ویژگی را با تعداد نقاط مهم محاسبه کنید
feature_vector = np.sum(dst > 0.01 * dst.max())
python
import cv2
import numpy as np
from skimage import filters

# خواندن تصویر
img = cv2.imread('fingerprint.png', 0)

# حذف نویز با استفاده از فیلتر میانگین
img = cv2.medianBlur(img, 5)

# بهبود کیفیت تصویر با استفاده از تبدیل هیستوگرام
img = cv2.equalizeHist(img)

# استخراج نقاط مهم با استفاده از الگوریتم Harris
dst = cv2.cornerHarris(img,2,3,0.04)

# نشان دادن نقاط مهم روی تصویر اصلی
img[dst>0.01*dst.max()]=[0]

# نشان دادن تصویر
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

python
import cv2
import numpy as np

# خواندن تصویر
img = cv2.imread('fingerprint.png')

# تبدیل تصویر به سطح خاکستری
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# استخراج ویژگی‌ها با استفاده از الگوریتم هریس
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

# استخراج مکان نقاط گوشه
x, y = np.where(dst > 0.01 * dst.max())
corners = zip(x, y)

# بردار ویژگی را با تعداد نقاط گوشه محاسبه کنید
feature_vector = len(corners)

python
from scipy.cluster.vq import kmeans, vq

# فرض می‌کنیم که بردار ویژگی‌ها در یک لیست به نام feature_vectors ذخیره شده است
# و تعداد کلستر‌ها یا کدبوک‌ها را به نام num_codebooks تعریف می‌کنیم

num_codebooks = 10
codebooks, distortion = kmeans(feature_vectors, num_codebooks)

# استفاده از کدبوک‌ها برای کوانتیزه کردن بردارهای ویژگی
codes, _ = vq(feature_vectors, codebooks)


python
from scipy.cluster.vq import vq

# فرض می‌کنیم که feature_vector بردار ویژگی اثر انگشت جدید و codebooks کدبوک‌های موجود در دیتابیس شما است

# استفاده از کدبوک‌ها برای کوانتیزه کردن بردار ویژگی
codes, _ = vq([feature_vector], codebooks)

# چک کردن اینکه آیا کدبوک متناظر با این بردار ویژگی در دیتابیس وجود دارد یا خیر
if codes[0] in database:
    print('Fingerprint recognized.')
else:
    print('Fingerprint not recognized.')