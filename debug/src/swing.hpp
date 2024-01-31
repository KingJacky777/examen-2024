class Swing
{
public:
    enum Type
    {
        babies,
        flat
    };
    float calculateHeight();
    Swing(int id, Type type, float rope);
    ~Swing() = default;
    int& getHorizontalPos(){
        return _horizontalPos;
    }
    void update(int = 1);

private:
    Type _type;
    float _ropeLength;
    int _id;
    int _horizontalPos = 0;
    int _direction = 0;
};